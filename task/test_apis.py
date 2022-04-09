import requests


username = input('Username of test user: ')
password = input('Password of test user: ')
current_host = input('Type protocol and host name like http://127.0.0.1:8000: ')
login_url = current_host + '/api/get-api-token/'
r = requests.post(login_url, {'username': username, 'password': password})
assert r.status_code == 200, r.json()

auth_token = r.json()['token']
token = 'Token ' + auth_token
headers = {'Authorization': token}


def test_get_todo_list_api():
    print('------- Testing get ToDO list delete API ---------')
    url = current_host + '/api/todo_list/'
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, r.json()
    print('Get ToDO list API tested successfully.')


def test_create_todo_api():
    print('------- Testing create todo item API ---------')
    url = current_host + '/api/todo_list/'
    title = input('Enter title of task: ')
    description = input('Enter description of task: ')
    due_date = input('Enter due date for task in yyyy-mm-dd format: ')
    data = {'description': description, 'title': title, 'due_date': due_date}
    response = requests.post(url, headers=headers, data=data)
    assert response.status_code == 201, print(response.json())
    print('Create ToDO item API tested successfully.')


def test_delete_todo_api():
    print('------- Testing delete ToDO item API ---------')
    pk = input('Enter the ID of todo item: ')
    url = current_host + '/api/todo_list/' + pk +'/'
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, "Invalid ToDo item ID"
    print('delete ToDO item API tested successfully.')


def test_update_todo_api():
    print('------- Testing update ToDO item API ---------')
    pk = input('Enter the ID of todo item: ')
    url = current_host + '/api/todo_list/' + pk + '/'
    title = input('Enter title of task: ')
    description = input('Enter description of task: ')
    state = input('Enter of new status of task P for in Progress and D for Done: ')
    data = {'title': title, 'description': description, 'state': state}
    response = requests.put(url, headers=headers, data=data)
    assert response.status_code == 201, response.json()
    print('------- update ToDO item API tested successfully ---------')


test_create_todo_api()
test_update_todo_api()
test_get_todo_list_api()
test_delete_todo_api()
