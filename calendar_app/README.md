# lab13-sprint-full-stack-slop-llc

# A Python-based command-line tool that allows users to manage personal tasks and automatically schedule them on their Google Calendar. Built using Agile practices, GitHub Flow, and full test coverage.


## Features:
# Add a task (title, description, start time, end time)
# View task list stored in memory
# Push task to Google Calendar via OAuth 2.0
# Returns event link on successful creation

# To run main:

# Set up Environment:
python3 -m venv venv
# Activate Environment: 
source venv/bin/activate
# Install google-auth-oauthlib
# While your virtual environment is still active ((venv) is visible), run:
pip install --break-system-packages google-auth-oauthlib
# Then to be safe, also:
pip install --break-system-packages google-api-python-client
# These are the two core dependencies for Google Calendar API access.


# Option 1 (recommended): Install locally and run from anywhere
# From the root of the project
pip install -e .
# Then run the app using the installed CLI command
calendar-app

# Option 2: Run without installing
# From project root
cd calendar_app
PYTHONPATH=calendar_app/src python3 -m calendar_app.main

# To run tests:
# source .venv/bin/activate

# PYTHONPATH=calendar_app/src pytest calendar_app/tests

# Run test_main.py (CLI tests)
PYTHONPATH=src pytest tests/test_main.py

# Run test_calendar_api.py (Google Calendar integration):
PYTHONPATH=src pytest tests/test_calendar_api.py

# Run test_task_manager.py (Task + TaskManager logic):
PYTHONPATH=src pytest tests/test_task_manager.py