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
    add_parser.add_argument('title', type=str, help='Name of the task')
    add_parser.add_argument("--priority", choices=["low", "medium", "high"],
                            help="Priority of the task", default="medium")
    add_parser.add_argument("--due", type=str, default=None)
    add_parser.set_defaults(func=add_task)

    # Subparser for list command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('--status', choices=["not started", "pending", "complete"],
                             default='not started', help="Completion status of the task")
    list_parser.add_argument('--priority', type=str, default=None)
    list_parser.add_argument('--due', type=str, default=None)
    list_parser.set_defaults(func=list_tasks)

    # Subparser for complete command
    complete_parser = subparsers.add_parser('complete')
    complete_parser.add_argument("id", type=int, help="ID of the task to mark complete")
    complete_parser.set_defaults(func=complete_task)

    # Subparser for delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")
    delete_parser.add_argument('title', type=str, help="Name of the task to delete")
    delete_parser.set_defaults(func=delete_task)

def add_task(args):
    return

def list_tasks(args):
    return

def complete_task(args):
    return

def delete_task(args):
    return