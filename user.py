# user.py

class User:
    def __init__(self, name, email):
        self.id = len(User.users) + 1
        self.name = name
        self.email = email
        self.tasks = []
        User.users.append(self)

    def add_task(self, task):
        self.tasks.append(task)

    def print_tasks(self):
        if not self.tasks:
            print(f"No tasks assigned to {self.name}.")
            return

        print(f"\nTasks assigned to {self.name}:")
        for task in self.tasks:
            print(task)

    @staticmethod
    def get_user_by_email(email):
        for user in User.users:
            if user.email == email:
                return user
        return None

User.users = []