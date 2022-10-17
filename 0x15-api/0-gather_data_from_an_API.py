#!/usr/bin/python3
"""
a script that returns info about a customer's todo list
"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        url = "https://jsonplaceholder.typicode.com"
        customer_id = argv[1]

        r = requests.get("{}/users/{}".format(url, customer_id)).json()



