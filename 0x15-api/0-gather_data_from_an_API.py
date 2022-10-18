#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get(url + "/todos", params={"userId": employee_id}).json()

    completed = [data.get('title')
                 for data in todos if data.get('completed') is True]

    total_number_of_task = len(todos)
    number_of_done_task = len(completed)
    employee_name = user.get('name')

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_task, total_number_of_task))
    [print("\t {}".format(title)) for title in completed]

# if __name__ == '__main__':
#     url = "https://jsonplaceholder.typicode.com"
#     user_id = argv[1]

#     params = {"userId": user_id}

#     r = requests.get("{}/users/{}".format(url, user_id)).json()
#     employee_todo = requests.get(url + "/todos", params).json()
#     employee_name = r.get('name')

#     completed_tasks = []
#     for data in employee_todo:
#         if (data.get('completed') is True):
#             data = data.get('title')
#             completed_tasks.append(data)

#     num_of_tasks = len(employee_todo)
#     tasks_done = len(completed_tasks)

#     print("Employee {} is done with tasks({}/{}):".format(employee_name,
#           tasks_done, num_of_tasks))

#     for title in completed_tasks:
#         print("\t {}".format(title))
