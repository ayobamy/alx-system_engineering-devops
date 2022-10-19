#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get("{}/users/{}".format(url, employeeId)).json()
    todos = requests.get(url + "/todos", params={"userId": employeeId}).json()

    userName = employee.get('username')
    fileName = employeeId + ".json"

    line = []
    for info in todos:
        info.append({'task': info.get('title'),  })

