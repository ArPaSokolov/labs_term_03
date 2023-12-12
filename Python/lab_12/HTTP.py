import requests

base_url = 'https://httpbin.org'

def make_request(method, path, headers=None, body=None, output_file=None):
    url = f'{base_url}{path}'

    response = None
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, json=body)
    elif method == 'OPTIONS':
        response = requests.options(url, headers=headers)

    if response is not None:
        print('Request:\n')
        print(f'Method: {method}\n')
        print(f'URL: {url}\n')
        print(f'Headers: {response.request.headers}\n')
        if method == 'GET' or method == 'POST':
            print(f'Body: {response.request.body}\n')

        print('\nResponse:\n')
        print(f'Status Code: {response.status_code}\n')
        print(f'Headers: {response.headers}\n')
        if method == 'GET' or method == 'POST':
            print(f'Body: {response.text}\n')


# Примеры
make_request('GET', '/get', output_file='output.txt')

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-Type': 'application/json'}

make_request('POST', '/post', headers=headers, body=payload, output_file='output.txt')

make_request('OPTIONS', '/get', output_file='output.txt')