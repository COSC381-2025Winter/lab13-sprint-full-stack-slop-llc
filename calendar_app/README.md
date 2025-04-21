# lab13-sprint-full-stack-slop-llc

# A Python-based command-line tool that allows users to manage personal tasks and automatically schedule them on their Google Calendar. Built using Agile practices, GitHub Flow, and full test coverage.


## Features:
# Add a task (title, description, start time, end time)
# View task list stored in memory
# Push task to Google Calendar via OAuth 2.0
# Returns event link on successful creation

To run main:
Option 1 (recommended): Install locally and run from anywhere
From the root of the project
pip install -e .

Then run the app using the installed CLI command
calendar-app

Option 2: Run without installing
From project root
cd calendar_app PYTHONPATH=calendar_app/src python3 -m calendar_app_package.main

To run tests:
source .venv/bin/activate
PYTHONPATH=calendar_app/src pytest calendar_app/tests
