#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employeeId = argv[1]

    employee = requests.get("{}/users/{}".format(url, employeeId)).json()
    todos = requests.get(url + "/todos", params={"userId": employeeId}).json()

    userName = employee.get('username')
    fileName = employeeId + ".csv"

    line = []
    for info in todos:
        line.append([employeeId, userName, info.get('completed'),
                    info.get('title')])

    with open(fileName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for r in line:
            writer.writerow(r)
