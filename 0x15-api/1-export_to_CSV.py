#!/usr/bin/python3
"""task #0, extend your python script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/user/{}"
                            .format(employee_id))
    name = employee.json().get('username')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    filename = employee_id + '.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todo_list.json():
            if task.get('userId') == int(employee_id):
                writer.writerow([employee_id, name, str(task.get('completed')),
                                task.get('title')])
