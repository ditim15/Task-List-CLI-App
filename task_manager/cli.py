import argparse
import datetime
from task_manager import storage
from task_manager.task import Task

def build_parser():
    parser = argparse.ArgumentParser(
        prog='task-manager',
        description='Add, update, delete, and manage tasks ',
        epilog='Thanks for using the %(prog)s!'
    )

    subparsers = parser.add_subparsers(dest="command")

    # Subparser for add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('title', type=str, help='Title of the task')
    add_parser.add_argument("--priority", choices=["low", "medium", "high"],
                            help="Priority of the task", default="medium")
    add_parser.add_argument("--due", type=str, default=None, help="Due date of the task")
    add_parser.set_defaults(func=add_task)

    # Subparser for list command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('--status', choices=["pending", "complete"],
                             default=None, help="Completion status of the task")
    list_parser.add_argument('--priority', choices=["low", "medium", "high"], default=None,
                             help="Priority of the task")
    list_parser.add_argument('--due', type=str, default=None, help="Due date of the task")
    list_parser.set_defaults(func=list_tasks)

    # Subparser for complete command
    complete_parser = subparsers.add_parser('complete')
    complete_parser.add_argument("id", type=int, help="ID of the task to mark complete")
    complete_parser.set_defaults(func=complete_task)

    # Subparser for delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")
    delete_parser.set_defaults(func=delete_task)

    # Subparser for edit command
    edit_parser = subparsers.add_parser('edit')
    edit_parser.add_argument("id", type=int, help="ID of the task to edit")
    edit_parser.add_argument('--title', type=str, default=None, help="Title of the task to edit")
    edit_parser.add_argument('--status', choices=["pending", "complete"],
                             help="Completion status of the task")
    edit_parser.add_argument('--priority', choices=["low", "medium", "high"], default=None,
                             help="Priority of the task")
    edit_parser.add_argument('--due', type=str, default=None, help="Due date of the task")
    edit_parser.set_defaults(func=edit_task)

    return parser

def add_task(args):
    tasks = storage.read_tasks()
    new_id = storage.get_next_id(tasks)
    date_created = datetime.datetime.now()
    date_string = date_created.strftime("%Y-%m-%d")
    new_task = Task(new_id, args.title, date_string, args.priority, due_date=args.due)

    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"Saved '{args.title}' to task list.")


def list_tasks(args):
    tasks = storage.read_tasks()
    if args.priority is not None:
        tasks = [task for task in tasks if task.priority == args.priority]
    if args.status is not None:
        tasks = [task for task in tasks if task.status == args.status]
    if args.due is not None:
        tasks = [task for task in tasks if task.due_date == args.due]
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def complete_task(args):
    tasks = storage.read_tasks()
    found = False
    for task in tasks:
        if task.id == args.id:
            task.status = "complete"
            task.date_completed = datetime.datetime.now().strftime("%Y-%m-%d")
            found = True
    if found:
        storage.save_tasks(tasks)
        print(f'Task {args.id} marked as completed.')
    else:
        print(f'Task {args.id} does not exist.')

def delete_task(args):
    tasks = storage.read_tasks()
    tasks_length = len(tasks)
    tasks = [task for task in tasks if task.id != args.id]
    if len(tasks) < tasks_length:
        storage.save_tasks(tasks)
        print(f'Task {args.id} deleted.')
    else:
        print(f'Task {args.id} does not exist.')

def edit_task(args):
    tasks = storage.read_tasks()
    found = False
    updated = False
    for task in tasks:
        if task.id == args.id:
            if args.title is not None:
                task.title = args.title
                updated = True
            if args.priority is not None:
                task.priority = args.priority
                updated = True
            if args.status is not None:
                task.status = args.status
                updated = True
            if args.due is not None:
                task.due_date = args.due
                updated = True
            found = True
    if not found:
        print(f'Task {args.id} does not exist.')
    elif not updated:
        print(f'Nothing was updated.')
    else:
        storage.save_tasks(tasks)
        print(f'Task {args.id} succesfully updated.')