class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def update(self, title=None, description=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description