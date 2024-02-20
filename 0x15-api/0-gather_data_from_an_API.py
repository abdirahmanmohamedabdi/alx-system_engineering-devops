#!/usr/bin/python3
"""script that, using the REST API, for a given employee ID,
returns information about his/her"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))
    name = employee.json().get('name')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed_tasks = 0
    for task in todo_list.json():
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_tasks, total_tasks))
    print('\n'.join(["\t " + tk.get('title') for tk in todo_list.json()
          if tk.get('userId') == int(employee_id) and tk.get('completed')]))
