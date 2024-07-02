<h1 align="center">
  <br>
  <a href="https://www.yogendrasinghrathore.in/"><img src="static/images/auto_bounty_pro_logo.png" width="200px" alt="Auto Bounty Pro"></a>
</h1>

<h4 align="center">Customizable, Robust Automation for Comprehensive Bug Bounty Hunting Tool</h4>

![Python](https://img.shields.io/badge/Python-3.11.4-Green
)
![Flask](https://img.shields.io/badge/Flask-3.0.3-Green
)
![PyYaml](https://img.shields.io/badge/PyYAM-6.0.1-Green
)
![DevMod](https://img.shields.io/badge/Dev_Mode-Under_Developemnt-Green
)
![Tool_Version](https://img.shields.io/badge/Auto_Bounty_Pro_Version-v0.1.0-Green
)

| :exclamation:  **Disclaimer**  |
|---------------------------------|
| **This project is in active development**. Expect breaking changes with releases. Review the release changelog before updating. |

## About Auto Bounty Pro

Auto Bounty Pro is an open-source, customizable, and robust automation tool designed to streamline the bug bounty hunting process. Built with flexibility and extensibility in mind, it allows security researchers and penetration testers to efficiently manage and automate various stages of their security assessments.

## Updates Table
| Update    | Status | Details | Version |
| -------- | ------- | ------- | ------- |
| YAML | Done  | Adding YAML to config the App and lots of Setting would be easy for any user(Even Noobs) to Customize the app | v0.1.0 |
| Flask App | Done | Using Flask for a lightweight web app | v0.1.0 |
| Docker | Done | Docker is for use to manage Hacking Tools and its Cross-Platform supports | v0.1.0 |
| Base Docker YAML | working | This YAML helps users to add and remove tools as per their requirements | v0.1.2 |
| Tool Registry | Done | Adding YAML Based Tool Registry to handel Install and Remove Tools | v0.1.0 |
| Plugin | Done | Allow User to create new Tools and plugin With Auto Bounty Pro | v0.1.0 |
| Dashbard | wrodking | Allow User view all activity and provide easy readibility | v0.1.5 |
| RestFul API | wrodking | Allow User to work with other and Access Tool Anyware | v0.2.0 |

### Key Features

- **Customizable Tool Integration**: Easily add or remove tools based on your specific requirements, categorize them, and integrate them into your workflow.
- **Robust Project Management**: Each project is self-contained, with its own scan outputs, input data, and reports, allowing for organized and efficient project handling.
- **Automation and Pipelines**: Automate repetitive tasks and create pipelines where the output of one tool can be used as the input for another, streamlining your workflow.
- **Local and Remote Access**: While primarily designed to run on a local machine, Auto Bounty Pro also supports remote access via a web interface, providing flexibility in how you work.
- **Integration with OWASP ZAP & Burp Suite**: Enhance your web application security testing with seamless integration with these powerful tools.
- **Wordlist Management**: Manage and use wordlists efficiently by installing them directly into the tool’s database.
- **Scripting and Cron Jobs**: Upload and run custom scripts (Python, Bash) and set up cron jobs for scheduled tasks to further enhance the tool's capabilities.
- **Server and API**: The tool can run its own server to provide a basic web app with a good user interface and RESTful API endpoints for interacting with other tools and systems.

### Mission

Our mission is to empower security researchers and penetration testers with a tool that not only simplifies and automates the bug bounty process but also adapts to their unique workflows and needs. By providing a flexible and robust platform, we aim to enhance productivity and efficiency in identifying and mitigating security vulnerabilities.

## Prerequisites
- Python 3.11.4
- Docker in Your Local Machine

## Installation
Clone Github Repo
  ```bash
    git clone git@github.com:yogendra-singh-rathore/Auto-Bounty-Pro.git
    
    cd Auto-Bounty-Pro

  ```
  Open CMD
  ```bash
    python -m venv autobounty

  ```
  Install requirement and run
  ```bash
  pip install -r requirements.txt
  python main.py
  ```

## Install Docker Based Web App
 ```bash
  docker pull m3evil/auto-bounty-pro:testimage
  docker container run -d -p 3000:3000 m3evil/auto-bounty-pro:testimage
  ```


## Donations
![Support](https://img.shields.io/badge/Support-Auto%20Bounty%20Pro%20-Green
)

Auto Bounty Pro gratefully accepts donations via Bitcoin and USDT. Your support helps us continue to develop and maintain this project. If you'd like to express your support for Auto Bounty Pro, please consider donating to the following addresses:

- **Bitcoin (BTC):** 1QLEhtmdxLb7qBGB4VeweCr3cw2fX9yuoC
- **USDT (TRC20):** TPJHAuYzFURjVNBbCcCifXL9YsgVYVRqNR

Thank you for supporting Auto Bounty Pro! Your donations help us cover development costs and keep the project running.

## Contributors

The core project team are:
- [Yogendra Singh Rathore](https://github.com/yogendra-singh-rathore/) 

Thanks to all the amazing [community contributors for sending PRs](https://github.com/yogendra-singh-rathore/Auto-Bounty-Pro/graphs/contributors) and keeping this project updated. :heart:

If you have an idea or some kind of improvement, you are welcome to contribute and participate in the Project, feel free to send your PR.

or
#### Read Auto Bounty Pro SRS
[![SRS](https://img.shields.io/badge/SRS-v1.0-Green)](https://github.com/yogendra-singh-rathore/Auto-Bounty-Pro/blob/main/srs.md)

To understand the detailed specifications and requirements of Auto Bounty Pro, you can read our comprehensive Software Requirements Specification (SRS) document. This document outlines the features, functionalities, and technical details of the project, providing an in-depth look at what Auto Bounty Pro offers and how it is designed.

By reviewing the SRS, you can gain insights into:
- The objectives and goals of Auto Bounty Pro
- Detailed descriptions of each feature and tool
- System architecture and design considerations
- User interface and experience guidelines
- Integration points with other tools and APIs

We encourage you to read the SRS to get a full understanding of the project's scope and capabilities.


<p align="center">
<a href="https://github.com/yogendra-singh-rathore/Auto-Bounty-Pro/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yogendra-singh-rathore/Auto-Bounty-Pro&max=500">
</a>
</p>

## License
[![license](https://img.shields.io/badge/License-MIT-green
)](LICENSE)

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).
