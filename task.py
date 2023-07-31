# task.py

import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = self.parse_date(due_date)
        self.priority = priority
        self.status = "To Do"
        self.assigned_to = None

    def parse_date(self, date_string):
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None

    def assign_to(self, user):
        self.assigned_to = user
        self.status = "In Progress"

    def complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\n" \
               f"Due Date: {self.due_date}\nPriority: {self.get_priority_text()}\n" \
               f"Status: {self.status}\nAssigned To: {self.assigned_to.name if self.assigned_to else 'Unassigned'}\n"

    def get_priority_text(self):
        if self.priority == 1:
            return "High"
        elif self.priority == 2:
            return "Medium"
        elif self.priority == 3:
            return "Low"
        else:
            return "Unknown Priority"