from manager import TaskManager
from calendar_api import GoogleCalendarAPI

def main():
    manager = TaskManager()
    calendar_api = GoogleCalendarAPI()

    print("Welcome to the Task Scheduler App")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            start_time = input("Start Time (YYYY-MM-DDTHH:MM:SS): ")
            end_time = input("End Time (YYYY-MM-DDTHH:MM:SS): ")

            task = manager.add_task(title, description, start_time, end_time)
            link = calendar_api.create_event(task)
            print(f"Task created and added to Google Calendar.\nEvent link: {link}")

        elif choice == '2':
            tasks = manager.list_tasks()
            for task in tasks:
                print(task)

        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
