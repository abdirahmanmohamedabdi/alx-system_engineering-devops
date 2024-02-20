#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = todo_list.json()
    todo_user = {}
    task_list = []
    for tk in todo_list:
        if tk.get('userId') == int(employee_id):
            task_dict = {"task": tk.get('title'),
                         "completed": tk.get('completed'),
                         "username": employee.json().get('username')}
            task_list.append(task_dict)
    todo_user[employee_id] = task_list
    filename = employee_id + '.json'
    with open(filename, 'w') as f:
        json.dump(todo_user, f)
