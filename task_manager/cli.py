import argparse
from task_manager import storage

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
    return

def list_tasks(args):
    return

def complete_task(args):
    return

def delete_task(args):
    return

def edit_task(args):
    return