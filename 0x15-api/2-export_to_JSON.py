#!/usr/bin/env python3

import sys
import requests
import json

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

def export_to_json(user_id, tasks):
    data = {
        "user_id": user_id,
        "tasks": []
    }
    for task in tasks:
        task_data = {
            "task": task.get("title", ""),
            "completed": task.get("completed", False)
        }
        data["tasks"].append(task_data)
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user = get_user(user_id)
    if user:
        tasks = get_tasks(user_id)
        if tasks:
            export_to_json(user_id, tasks)
