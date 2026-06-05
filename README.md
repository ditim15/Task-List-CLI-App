# Task-List-CLI-App
Task list app made using Python through a command-line interface.

## Requirements
- Python 3.10 or higher

## Installation

Clone the repository:

```bash
git clone https://github.com/ditim15/Task-List-CLI-App.git
cd task-manager
```

Create and Activate a Virtual Environment
# Windows
Create a virtual environment.
```bash
python -m venv .venv
.venv\Scripts\activate
```
Then install the package 
```bash
pip install -e .
```
# Mac/Linux
Same idea for Mac/Linux, create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

Then install the package 
```bash
pip install -e .
```

## Usage

Adding a task:
```bash
tasks add "wash dishes"
tasks add "take out the trash" --priority low
tasks add "do homework" --due 2026-06-10
```

Listing tasks:
```bash
tasks list
tasks list --status complete
tasks list --priority high
tasks list --due 2026-06-12
```

Mark task as complete:
```bash
tasks complete 1
```

Delete a task:
```bash
tasks delete 1
```

Edit a task:
```bash
tasks edit 1 --title "new task name" --priority low
```

For additional help:
```bash
tasks --help
```

