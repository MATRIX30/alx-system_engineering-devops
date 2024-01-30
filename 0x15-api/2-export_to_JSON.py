#!/usr/bin/python3
"""python script to fetch employee information from their ID
   using an api
"""

if __name__ == "__main__":
    import json
    from os import sys
    from requests import get

    employee_ID = sys.argv[1]
    json_file = "{}.json".format(employee_ID)
    user_info = get("https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_ID))
    user_name = (user_info.json()[0].get('username'))
    todos = get("https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_ID))

    user_info = {"{}".format(employee_ID): []}

    for todo in todos.json():
        task = {"task": f"{todo.get('title')}",
                "completed": todo.get('completed'),
                "username": f"{user_name}"}
        user_info.get("{}".format(employee_ID)).append(task)
    with open(json_file, 'w') as f:
        json.dump(user_info, f)
