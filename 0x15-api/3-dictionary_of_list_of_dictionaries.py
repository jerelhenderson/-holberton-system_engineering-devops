#!/usr/bin/python3
""" return information about employees TODO list using JSON """
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    employees = requests.get('{}/users'.format(url)).json()

    for employee in employees:
        employee_id = employee.get('id')
        tasks = requests.get("{}/users/{}/todos".format(url,
                                                employee.get('id'))).json()
        list_tasks = []

        dict_tasks = {}
        for task in tasks:
            if task.get('userId') == employee_id:
                list_tasks.append({'task': task.get('title'), 'completed':
                        task.get('completed'), 'username': task.get('name')})
                dict_tasks["{}".format(employee_id)] = list_tasks

    with open('todo_all_employees.json', 'w') as file:
        json_dict = json.dumps(dict_tasks)
        file.write(json_dict)
