import sqlite3

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('assets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS assets (
                    id INTEGER PRIMARY KEY,
                    program_name TEXT NOT NULL,
                    platform_name TEXT NOT NULL,
                    volume_name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()