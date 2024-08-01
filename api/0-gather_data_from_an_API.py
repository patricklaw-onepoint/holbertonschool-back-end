#!/usr/bin/python3
"""Script that uses https://jsonplaceholder.typicode.com/ for a
given employee ID, returns information about his/her todo list progress."""
from sys import argv
import requests

if __name__ == "__main__":
    employeeId = argv[1]

    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users/{employeeId}"
    todoUrl = f"{baseUrl}/users/{employeeId}/todos"

    name = requests.get(userUrl, timeout=10).json()["name"]

    todo = requests.get(todoUrl, timeout=10).json()
    tasks = [task["title"] for task in todo if task["completed"]]

    completed = len(tasks)
    total = len(todo)

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for title in tasks:
        print(f"\t {title}")
