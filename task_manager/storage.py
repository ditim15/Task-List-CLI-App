import json
from task_manager.task import Task

FILE = "tasks.json"

def read_tasks():
    try:
        with open(FILE, "r") as f:
            return [Task.from_dict(task) for task in json.load(f)]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    task_list = [task.to_dict(task) for task in tasks]
    with open(FILE, "w") as f:
        json.dump(task_list, f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return tasks[-1].id + 1