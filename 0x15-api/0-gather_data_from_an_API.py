#!/usr/bin/python3
"""python script to fetch employee information from their ID
   using an api
"""

if __name__ == "__main__":
    from os import sys
    from requests import get

    employee_ID = sys.argv[1]
    user_info = get("https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_ID))
    user_name = (user_info.json()[0].get('name'))
    todos = get("https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_ID))
    number_of_task = len(todos.json())

    number_of_completed_task = 0
    for todo in todos.json():
        if todo.get('completed'):
            number_of_completed_task += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, number_of_completed_task, number_of_task))
    for todo in todos.json():
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
