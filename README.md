# Notes
## Folder Structure
**po**: This folder contains the page objects for this project

**test**: This folder contains the bug report and associated files

**webdrivers**: This folder contains the webdrivers for Chrome and Firefox browsers

## Other Files
**localhost_tester.py**: The starter script for the automated test

**env**: This file is used to store localized environment variables

## .env Settings
**ACCOUNT_USER**: Change this to a test account name

**ACCOUNT_PASSWORD**: Add the password here

**FIREFOX_PROFILE**: This is the path to the firefox profile used to run the browser.
    To replace the value with the local path, copy its value up to "Profiles", press Win+R, 
    type %APPDATA%, paste the value and press Enter.

## Installation Procedures
### Prerequisites
1. Python 3.8+ (3.7 can also work)
2. Git

### Steps
1. Create a folder to contain the repo
2. Navigate to https://github.com/reywald/part-one
3. Clone the repo to the folder in (1).
4. Create a folder _.venv_ to contain the virtual environment
5. Open the folder and run the following commands
    * **_python -m pip install pipenv_**
    * **_pipenv install_**
    * **_pipenv shell_**
    * **_python -m unittest_**
