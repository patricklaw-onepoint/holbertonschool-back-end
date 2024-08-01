#!/usr/bin/python3
"""Script that uses https://jsonplaceholder.typicode.com/ for a
given employee ID, returns information about his/her todo list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    employeeId = argv[1]

    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users/{employeeId}"
    todoUrl = f"{baseUrl}/users/{employeeId}/todos"

    userResponse = requests.get(userUrl, timeout=10)
    name = userResponse.json()["name"]

    todoResponse = requests.get(todoUrl, timeout=10)
    todoData = todoResponse.json()
    tasks = [task["title"] for task in todoData if task["completed"]]

    completed = len(tasks)
    total = len(todoData)

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for title in tasks:
        print(f"\t {title}")
