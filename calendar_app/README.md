# lab13-sprint-full-stack-slop-llc

# A Python-based command-line tool that allows users to manage personal tasks and automatically schedule them on their Google Calendar. Built using Agile practices, GitHub Flow, and full test coverage.

## Features:
# Add a task (title, description, start time, end time)
# View task list stored in memory
# Push task to Google Calendar via OAuth 2.0
# Returns event link on successful creation

# To run main:
From the root of the project
cd calendar_app
# Set up Environment:
python3 -m venv venv
# Activate Environment: 
source venv/bin/activate
# Install google-auth-oauthlib
# While your virtual environment is still active ((venv) is visible), run:
pip install --break-system-packages google-auth-oauthlib
pip install --break-system-packages pytest-cov
pip install --break-system-packages google-api-python-client

# These are the three core dependencies for Google Calendar API access.

# After this, run the following command to start the program!
PYTHONPATH=src python3 -m calendar_app_package.main


### Testing
# do the steps up until youre going to run the program, but instead run
python3 -m pytest --cov=calendar_app_package
# this will show 100% test coverage