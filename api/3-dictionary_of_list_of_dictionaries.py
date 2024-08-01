#!/usr/bin/python3
"""Script that uses https://jsonplaceholder.typicode.com/ for
all employees, export data in the JSON format."""
from sys import argv
import json
import requests

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com"
    usersUrl = f"{baseUrl}/users"

    users = requests.get(usersUrl, timeout=10).json()

    dic = {}

    for user in users:
        employeeId = user["id"]
        todoUrl = f"{baseUrl}/users/{employeeId}/todos"
        todo = requests.get(todoUrl, timeout=10).json()

        newList = []
        for task in todo:
            newList.append(
                {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"],
                }
            )

        dic[employeeId] = newList

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(dic, f)
