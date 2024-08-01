#!/usr/bin/python3
"""Script that uses https://jsonplaceholder.typicode.com/ for a
given employee ID, export data in the JSON format."""
from sys import argv
import json
import requests

if __name__ == "__main__":
    employeeId = argv[1]

    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users/{employeeId}"
    todoUrl = f"{baseUrl}/users/{employeeId}/todos"

    user = requests.get(userUrl, timeout=10).json()
    todo = requests.get(todoUrl, timeout=10).json()

    dic = {employeeId: []}

    for task in todo:
        dic[employeeId].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
        )

    with open(f"{employeeId}.json", "w", encoding="utf-8") as f:
        json.dump(dic, f)
