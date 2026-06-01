class Task:
    def __init__(self, id, title, date_created, priority,status="pending", due_date=None, date_completed=None):
        self.id = id
        self.title = title
        self.status = status
        self.date_created = date_created
        self.priority = priority
        self.due_date = due_date
        self.date_completed = date_completed

        