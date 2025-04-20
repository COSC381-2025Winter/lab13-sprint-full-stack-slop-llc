import pytest
from calendar_app_package import main as app_main

def test_cli_add_task_and_exit(monkeypatch, capsys):
    inputs = iter([
        '1',                      # Select "Add Task"
        'Test Task',             # Title
        'Test Description',      # Description
        '04/20/2025 10:00 AM',   # Start time
        '04/20/2025 11:00 AM',   # End time
        '3'                      # Exit
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    class MockCalendarAPI:
        def create_event(self, task):
            return "https://calendar.google.com/fake-link"

    monkeypatch.setattr("calendar_app_package.main.calendar_api", MockCalendarAPI)

    app_main.main()
    output = capsys.readouterr().out
    assert "Task created and added to Google Calendar." in output
    assert "https://calendar.google.com/fake-link" in output

def test_cli_view_tasks_and_exit(monkeypatch, capsys):
    inputs = iter(['2', '3'])  # View → Exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    class MockTask:
        def __str__(self):
            return "Mock Task: 2025-04-21T10:00:00 → 2025-04-21T11:00:00"

    class MockTaskManager:
        def __init__(self):
            pass
        def list_tasks(self):
            return [MockTask()]
        def add_task(self, *args, **kwargs):
            return MockTask()

    class MockCalendarAPI:
        def create_event(self, task):
            return "https://calendar.google.com/fake-link"

    # ✅ Correct patching based on actual class names used in main.py
    monkeypatch.setattr("calendar_app_package.main.TaskManager", MockTaskManager)
    monkeypatch.setattr("calendar_app_package.main.calendar_api", MockCalendarAPI)

    app_main.main()

    output = capsys.readouterr().out
    assert "Task List:" in output
    assert "Mock Task" in output

def test_cli_add_task_invalid_time(monkeypatch, capsys):
    """
    ✅ Test that entering an invalid date format triggers an error message
    """
    inputs = iter([
        '1',                      # Add Task
        'Broken Task',           # Title
        'Bad date format',       # Description
        'April 30 2pm',          # Invalid start time
        'April 30 3pm',          # Invalid end time
        '3'                      # Exit
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    class MockCalendarAPI:
        def create_event(self, task):
            return "https://calendar.google.com/fake-link"

    class MockTaskManager:
        def __init__(self): pass
        def add_task(self, *args, **kwargs):
            return MagicMock()
        def list_tasks(self):
            return []

    from calendar_app_package import main as app_main
    monkeypatch.setattr("calendar_app_package.main.TaskManager", MockTaskManager)
    monkeypatch.setattr("calendar_app_package.main.calendar_api", MockCalendarAPI)

    app_main.main()
    output = capsys.readouterr().out

    assert "Invalid format" in output or "Failed to create task" in output

