import json
from task_manager.task import Task

FILE = "tasks.json"

def read_tasks():
    try:
        with open(FILE, "r") as f:
            return [Task.from_dict(task) for task in json.load(f)]
    except FileNotFoundError:
        return []
