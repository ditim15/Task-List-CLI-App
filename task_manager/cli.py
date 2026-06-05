import argparse
from task_manager import storage

def build_parser():
    parser = argparse.ArgumentParser(
        prog='task-manager',
        description='Add, update, delete, and manage tasks ',
        epilog='Thanks for using the %(prog)s!'
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('title', type=str, help='Name of the task')
    add_parser.add_argument("--priority", choices=["low", "medium", "high"],
                            help="Priority of the task", default="medium")
    add_parser.add_argument("--due", type=str, default=None)
    add_parser.set_defaults(func=add_task)

def add_task():
    return