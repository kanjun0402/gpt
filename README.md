# Simple ToDo CLI

This repository contains a simple command line ToDo application written in Python.

## Usage

1. Add a new task:

   ```bash
   python3 todo.py add "Buy milk"
   ```

2. List tasks:

   ```bash
   python3 todo.py list
   ```

   Use `--all` to show completed tasks as well.

3. Mark a task as done:

   ```bash
   python3 todo.py done <task_id>
   ```

4. Remove a task:

   ```bash
   python3 todo.py rm <task_id>
   ```

5. Clear all tasks:

   ```bash
   python3 todo.py clear
   ```

Tasks are stored in `tasks.json` in the current directory.
