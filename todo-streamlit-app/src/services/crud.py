tasks_db = []

def create_task(tasks, title, description):
    task_id = len(tasks) + 1
    new_task = {
        'id': task_id,
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    return new_task

def get_tasks():
    return tasks_db

def update_task(tasks, task_id, title=None, description=None, completed=None):
    for task in tasks:
        if task['id'] == task_id:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            return task
    return None

def delete_task(tasks, task_id):
    for index, task in enumerate(tasks):
        if task['id'] == task_id:
            return tasks.pop(index)
    return None