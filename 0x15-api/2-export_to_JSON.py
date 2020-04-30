#!/usr/bin/python3
""" returns information about employees TODO list using JSON """
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]

    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos?userId={}'.format(url, employee_id)).json()

    list_tasks = []
    for task in tasks:
        list_tasks.append({"task": task.get('title'), 'completed':
                    task.get('completed'), 'username': employee.get('name')})

    dict_tasks = {}
    dict_tasks["{}".format(employee_id)] = list_tasks
    with open("{}.json".format(employee_id), 'w') as file:
        json_dict = json.dumps(dict_tasks)
        file.write(json_dict)
