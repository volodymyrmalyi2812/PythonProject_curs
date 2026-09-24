import json

import urllib3

HOST = '127.0.0.1:8000'


def get_url(path):
    return 'http://{host}{path}'.format(host=HOST, path=path)


def issue_url(pk):
    return get_url('/api/issues/{id}/'.format(id=pk))


issues_url = get_url('/api/issues/')
login_url = get_url('/api/auth/login/')
logout_url = get_url('/api/auth/logout/')

# створюємо `PoolManager` для кешування, використовуючи num_pools - кількість з'єднань, які кешуватимуться.
# варто відзначити, що requests використовує той же `urllib3` pool manager.
pool = urllib3.PoolManager(num_pools=4)

response = pool.request('GET', issues_url)
print(response)

login_credentials = {'username': 'test_user', 'password': 'test_pass'}
# надсилаємо POST-запит на login_url, використовуючи pool manager
response = pool.request('POST', login_url, fields=login_credentials)

# копіюємо cookies із заголовка (використовуємо явне ім'я заголовка)
cookie = response.headers['Set-Cookie']

# надсилаємо GET запит додаючи отримані cookies до запиту.
response = pool.request('GET', issues_url, headers={'Cookie': cookie})
parsed_data = json.loads(response.data.decode())
print(parsed_data)

# спроба передачі файлу (читаємо з диска та намагаємося передати на сервер)
with open('example7_urllib3.py', 'r') as f:
    content = f.read()

print('File content', content)
# формуємо дані для запиту
data = {'text_file': ('example.txt', content, 'text/plain')}
response = pool.request('POST', issues_url, fields=data,
                        headers={'Cookie': cookie})
print(response.status)
print(response.data)

# передаємо дані у форматі json на сервер методом POST.
login_credentials = json.dumps({
    'username': 'test_user',
    'password': 'test_pass'
}).encode()
response = pool.request('POST', login_url, body=login_credentials,
                        headers={'Content-Type': 'application/json'})
print(response.data)
print(cookie)
cookie = response.headers['Set-Cookie']
