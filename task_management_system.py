# task_management_system.py

from task import Task
from user import User

class TaskManagementSystem:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        priority = int(input("Enter task priority (1 - High, 2 - Medium, 3 - Low): "))

        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print("Task added successfully!")

    def edit_task(self):
        task_id = int(input("Enter the ID of the task you want to edit: "))

        for task in self.tasks:
            if task.id == task_id:
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                due_date = input("Enter new due date (YYYY-MM-DD): ")
                priority = int(input("Enter new task priority (1 - High, 2 - Medium, 3 - Low): "))

                task.title = title
                task.description = description
                task.due_date = due_date
                task.priority = priority
                print("Task edited successfully!")
                break
        else:
            print("Task not found!")

    def delete_task(self):
        task_id = int(input("Enter the ID of the task you want to delete: "))

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                break
        else:
            print("Task not found!")

    def assign_task(self):
        task_id = int(input("Enter the ID of the task you want to assign: "))
        user_id = int(input("Enter the ID of the user you want to assign the task to: "))

        task = self.find_task_by_id(task_id)
        user = self.find_user_by_id(user_id)

        if task and user:
            task.assign_to(user)
            print("Task assigned successfully!")
        else:
            print("Task or user not found!")

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nAll Tasks:")
        for task in self.tasks:
            print(task)

    def view_user_tasks(self):
        user_id = int(input("Enter the ID of the user you want to view tasks for: "))
        user = self.find_user_by_id(user_id)

        if user:
            user.print_tasks()
        else:
            print("User not found!")

    def view_statistics(self):
        if not self.tasks:
            print("No tasks found.")
            return

        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        in_progress_tasks = sum(1 for task in self.tasks if task.status == "In Progress")

        print("\nStatistics:")
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed Tasks: {completed_tasks}")
        print(f"In Progress Tasks: {in_progress_tasks}")

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None