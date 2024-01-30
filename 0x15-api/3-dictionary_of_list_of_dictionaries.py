#!/usr/bin/python3
"""python script to fetch employee information from their ID
   using an api
"""

if __name__ == "__main__":
    import json
    from requests import get

    json_file = "todo_all_employees.json"
    users_info = get("https://jsonplaceholder.typicode.com/users")
    todos = get("https://jsonplaceholder.typicode.com/todos")

    all_employee_todos = {}

    for user in users_info.json():
        user_task = []
        user_id = "{}".format(user.get('id'))
        for todo in todos.json():
            if todo.get('userId') == user.get('id'):
                user_task.append(
                    {"username": "{}".format(user.get('username')),
                     "task": "{}".format(todo.get('title')),
                     "completed": todo.get('completed')})

        all_employee_todos[user_id] = user_task

    with open(json_file, 'w') as f:
        json.dump(all_employee_todos, f)
