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

    r = requests.get("{}/users/{}".format(url, user_id)).json()
    user_todo = requests.get(url + "/todos", params).json()

    completed_tasks = [data.get('title')
                 for data in user_todo if data.get('completed') is True]
    # completed_tasks = []
    # for data in user_todo:
    #     if (data.get('completed')):
    #         data = data.get('title')
    #         completed_tasks.append(data)

    num_of_tasks = len(user_todo)
    tasks_done = len(completed_tasks)
    employee_name = r.get('name')

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          tasks_done, num_of_tasks))

    for title in completed_tasks:
        print("\t {}".format(title))
