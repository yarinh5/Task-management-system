# main.py

from task_management_system import TaskManagementSystem

def print_menu():
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Assign Task")
    print("5. View All Tasks")
    print("6. View User's Tasks")
    print("7. View Statistics")
    print("8. Exit")

def main():
    tms = TaskManagementSystem()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            tms.add_task()

        elif choice == "2":
            tms.edit_task()

        elif choice == "3":
            tms.delete_task()

        elif choice == "4":
            tms.assign_task()

        elif choice == "5":
            tms.view_all_tasks()

        elif choice == "6":
            tms.view_user_tasks()

        elif choice == "7":
            tms.view_statistics()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()