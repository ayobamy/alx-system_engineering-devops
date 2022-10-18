#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]

    params = {"userId": user_id}

    r = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id))
    todos = todos.json()
    employee_name = r.get('name')

    completed_tasks = []
    for data in todos:
        if (data.get('completed') is True):
            completed_tasks.append(data)

    total_num_of_tasks = len(todos)
    num_of_tasks_done = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_of_tasks_done, total_num_of_tasks))

    for title in completed_tasks:
        print("\t {}".format(title.get("title")))
