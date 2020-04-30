#!/usr/bin/python3
""" returns information about employee TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]

    employee = requests.get("{}/users/{}".format(url, employee_id)).json()
    tasks = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    finished_tasks = []
    for task in tasks:
        if task.get('completed') is True:
                    finished_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
                                                    finished_tasks, len(tasks)))
    for task in finished_tasks:
        print('\t', end="")
