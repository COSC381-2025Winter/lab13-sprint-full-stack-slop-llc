# lab13-sprint-full-stack-slop-llc

# To run main:

# Option 1 (recommended): Install locally and run from anywhere
# From the root of the project
pip install -e .
# Then run the app using the installed CLI command
calendar-app

# Option 2: Run without installing
# From project root
cd calendar_app
PYTHONPATH=calendar_app/src python3 -m calendar_app_package.main

# To run tests:
# source .venv/bin/activate
# PYTHONPATH=calendar_app/src pytest calendar_app/tests