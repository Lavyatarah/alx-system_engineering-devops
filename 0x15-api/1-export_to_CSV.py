#!/usr/bin/env python3

import sys
import requests
import csv

def get_user(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to retrieve user {}".format(user_id))
        return None

def get_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to retrieve tasks for user {}".format(user_id))
        return None

def export_to_csv(user_id, tasks):
    fieldnames = ["username", "task", "completed"]
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "username": user_id,
                "task": task.get("title", ""),
                "completed": task.get("completed", False)
            })

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user = get_user(user_id)
    if user:
        tasks = get_tasks(user_id)
        if tasks:
            export_to_csv(user_id, tasks)
