#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = todo_list.json()
    all_todos = {}
    for user in users:
        task_list = []
        for task in todo_list:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_dict)
        all_todos[user.get('id')] = task_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_todos, f)
