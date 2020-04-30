#!/usr/bin/python3
""" returns information about employees TODO list progress using CSV """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]

    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos?userId={}'.format(url, employee_id)).json()

    with open("{}.csv".format(employee_id), 'w') as file:
        for task in tasks:
            csv_f = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_f.writerow([str(employee_id), str(employee.get('name')),
                            str(task.get('completed')), str(task.get('title'))])
