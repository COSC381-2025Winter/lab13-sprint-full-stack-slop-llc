from .manager import TaskManager
from .calendar_api import calendar_api

def main():
    manager = TaskManager()
    calendar = calendar_api()

    print("Welcome to the Task Scheduler App")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            title = input("Task Title: ").strip()
            description = input("Task Description: ").strip()
            start_time = input("Start Time (YYYY-MM-DDTHH:MM:SS): ").strip()
            end_time = input("End Time (YYYY-MM-DDTHH:MM:SS): ").strip()

            try:
                task = manager.add_task(title, description, start_time, end_time)
                link = calendar.create_event(task)
                print("\nTask created and added to Google Calendar.")
                print(f"Event link: {link}")
            except Exception as e:
                print(f"\nFailed to create task or event: {e}")

        elif choice == '2':
            tasks = manager.list_tasks()
            if tasks:
                print("\nTask List:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks added yet.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()