#!/usr/bin/env python3
"""Simple CLI ToDo application."""

import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(description):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": task_id, "task": description, "done": False})
    save_tasks(tasks)
    print(f"Added task {task_id}: {description}")

def list_tasks(show_all):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        if not show_all and t["done"]:
            continue
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']:3} {status} {t['task']}")

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done")
            return
    print(f"Task {task_id} not found")

def remove_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found")
        return
    save_tasks(new_tasks)
    print(f"Removed task {task_id}")

def clear_tasks():
    save_tasks([])
    print("Cleared all tasks")

def main():
    parser = argparse.ArgumentParser(description="ToDo CLI")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("description", nargs="+", help="Task description")

    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("--all", action="store_true", help="Show all tasks including done")

    done_p = sub.add_parser("done", help="Mark task as done")
    done_p.add_argument("id", type=int, help="Task ID")

    rm_p = sub.add_parser("rm", help="Remove a task")
    rm_p.add_argument("id", type=int, help="Task ID")

    sub.add_parser("clear", help="Clear all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(" ".join(args.description))
    elif args.command == "list":
        list_tasks(args.all)
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "rm":
        remove_task(args.id)
    elif args.command == "clear":
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
