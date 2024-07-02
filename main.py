from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import subprocess
import yaml

app = Flask(__name__)

docker_volume = ""

def load_registry():
    with open('./yaml/registry.yaml', 'r') as file:
        return yaml.safe_load(file)

def save_registry(data):
    with open('./yaml/registry.yaml', 'w') as file:
        file.write("tools:\n")
        for category in data['tools']:
            file.write(f"  {category}:\n")
            for tool in data['tools'][category]:
                file.write(f"    - name: {tool['name']}\n")
                file.write(f"      description: {tool['description']}\n")
                file.write(f"      docker_image: {tool['docker_image']}\n")

def load_prostore():
    with open('./yaml/prostore.yaml', 'r') as file:
        return yaml.safe_load(file)

def save_prostore(data):
    with open('./yaml/prostore.yaml', 'w') as file:
        yaml.safe_dump(data, file)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/assets', methods=['GET'])
def assets():
    conn = sqlite3.connect('assets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assets")
    assets = c.fetchall()
    conn.close()

    return render_template('assets.html', assets=assets)

@app.route('/add_asset', methods=['POST'])
def add_asset():
    program_name = request.form['program_name']
    platform_name = request.form['platform_name']
    volume_name = f"{program_name.lower()}_{platform_name.lower()}"

    conn = sqlite3.connect('assets.db')
    c = conn.cursor()
    c.execute("INSERT INTO assets (program_name, platform_name, volume_name) VALUES (?, ?, ?)",
              (program_name, platform_name, volume_name))
    conn.commit()
    conn.close()

    # Create Docker volume
    subprocess.run(['docker', 'volume', 'create', volume_name])

    return redirect(url_for('assets'))

@app.route('/delete_asset', methods=['POST'])
def delete_asset():
    volume_name = request.form['volume_name']

    conn = sqlite3.connect('assets.db')
    c = conn.cursor()
    c.execute("DELETE FROM assets WHERE volume_name = ?", (volume_name,))
    conn.commit()
    conn.close()

    subprocess.run(['docker', 'volume', 'rm', volume_name])
    return redirect(url_for('assets'))

@app.route('/whatsnew')
def whatsnew():
    return render_template('whatsnew.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/prostore')
def prostore():
    prostore_data = load_prostore()
    return render_template('prostore.html', docker_images=prostore_data['docker_images'])

@app.route('/install_image', methods=['POST'])
def install_image():
    image_name = request.form['image_name']
    category = request.form['category']
    tools = request.form['tools'].split(',')
    prostore_data = load_prostore()
    registry_data = load_registry()
    print(registry_data)
    
    for image in prostore_data['docker_images']:
        if image['image_name'] == image_name:
            subprocess.run(['docker', 'pull', image_name])
            image['install_status'] = 'install'
            break

    if category not in registry_data['tools']:
        registry_data['tools'][category] = []

    for tool in tools:
        if not any(item['name'] == tool for item in registry_data['tools'][category]):
            registry_data['tools'][category].append({
                'name': tool,
                'description': f"Description for {tool}",
                'docker_image': image_name
            })

    save_prostore(prostore_data)
    save_registry(registry_data)
    return redirect(url_for('prostore'))

@app.route('/uninstall_image', methods=['POST'])
def uninstall_image():
    image_name = request.form['image_name']
    category = request.form['category']
    tools = request.form['tools'].split(',')
    prostore_data = load_prostore()
    registry_data = load_registry()

    for image in prostore_data['docker_images']:
        if image['image_name'] == image_name:
            subprocess.run(['docker', 'rmi', image_name])
            image['install_status'] = 'uninstall'
            break

    if category in registry_data['tools']:
        registry_data['tools'][category] = [
            tool for tool in registry_data['tools'][category] if tool['name'] not in tools
        ]

    save_prostore(prostore_data)
    save_registry(registry_data)
    return redirect(url_for('prostore'))

@app.route('/save_docker_volume', methods=['POST'])
def save_docker_volume():
    global docker_volume
    docker_volume = request.form['volume_name']
    print(docker_volume)
    return jsonify({'status': 'success', 'docker_volume': docker_volume})

@app.context_processor
def inject_tools():
    registry = load_registry()
    return dict(tools=registry['tools'])

if __name__ == '__main__':
    app.run(debug=True)
