class Task:
    def __init__(self, id, title, date_created, priority,status="pending", due_date=None, date_completed=None):
        self.id = id
        self.title = title
        self.status = status
        self.date_created = date_created
        self.priority = priority
        self.due_date = due_date
        self.date_completed = date_completed

    def __str__(self):
        return (f"Task {self.id}, '{self.title}', was created {self.date_created}\n"
                f"Priority: {self.priority}\n Status: {self.status}\n"
                f"Due date: {self.due_date}\n Completed date: {self.date_completed}")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date_created": self.date_created,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "date_completed": self.date_completed
        }