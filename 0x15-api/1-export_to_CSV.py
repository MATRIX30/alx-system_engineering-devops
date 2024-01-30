#!/usr/bin/python3
"""python script to fetch employee information from their ID
   using an api
"""

if __name__ == "__main__":
    from os import sys
    from requests import get

    employee_ID = sys.argv[1]
    csv_file = "{}.csv".format(employee_ID)
    user_info = get("https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_ID))
    user_name = (user_info.json()[0].get('username'))
    todos = get("https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_ID))

    with open(csv_file, 'w') as f:
        # csv_writer = csv.writer(f)
        # csv_writer.writerows(data)
        for todo in todos.json():
            f.write('"{}","{}","{}","{}"\n'.format(
             employee_ID, user_name, todo.get('completed'), todo.get('title')))
