#!/usr/bin/python3
"""Script that uses https://jsonplaceholder.typicode.com/ for a
given employee ID, export data in the CSV format."""
from sys import argv
import csv
import requests

if __name__ == "__main__":
    employeeId = argv[1]

    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users/{employeeId}"
    todoUrl = f"{baseUrl}/users/{employeeId}/todos"

    user = requests.get(userUrl, timeout=10).json()
    todo = requests.get(todoUrl, timeout=10).json()

    with open(
        f"{employeeId}.csv", mode="w", newline="", encoding="utf-8"
    ) as csvfile:
        csv_writer = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        for task in todo:
            csv_writer.writerow(
                [
                    user["id"],
                    user["username"],
                    task["completed"],
                    task["title"],
                ]
            )
