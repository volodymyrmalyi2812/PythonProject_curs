import json

import requests
from requests.adapters import HTTPAdapter

HOST = '127.0.0.1:8000'


def get_url(path):
    return 'http://{host}{path}'.format(host=HOST, path=path)


issues_url = get_url('/api/issues/')
login_url = get_url('/api/auth/login/')
logout_url = get_url('/api/auth/logout/')


def issue_url(pk):
    return get_url('/api/issues/{id}/'.format(id=pk))


# get issues (error)
# запитуємо http://127.0.0.1:8000/api/issues/ як неавторизований користувач
response = requests.get(issues_url)
print(response.status_code)
# `response.json()` - перетворює формат JSON на словник.
print(response.json())

# спроба авторизуватися, використовуючи вже наявні login/password
# test_user/test_pass вже створено, тому ми можемо їх використати.
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
# виконуємо запит і перевіряємо відповіді- ми авторизовані, у разі коректних username, password
response = requests.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

# копіюємо cookies з відповіді.
# сервер використовує cookies для зберігання `sessionid`, який також зберігається на сервері.
# За допомогою даного cookie сервер може визначити, чи авторизований користувач з даними `sessionid`.
# `sessionid` стає авторизованим після звернення до `login_url`.
cookies = response.cookies

# передаємо cookies у наступні запити, щоб сервер сприймав нас як користувача `test_user`.
response = requests.get(issues_url, cookies=cookies)
print(response.status_code)
print(response.json())

# спроба створити нову нотатку на сервері з порожнім тілом запиту, використовуючи
# POST запит з авторизованим `sessionid` у cookies.
response = requests.post(issues_url, cookies=cookies)
# Оскільки ми не передаємо даних для створення нотатки (name, description,
# due_date), то сервер поверне статус 400 і створить нотатку.
print(response.status_code)
print(response.json())

# готуємо дані для надсилання на сервер
issue_data = {'name': 'Buy Python Book',
              'due_date': '2009-02-11',
              'description': 'We have to buy a Python book!!!'}

# створюємо нотатку на сервері.
response = requests.post(issues_url, data=json.dumps(issue_data),
                         headers=headers, cookies=cookies)
# збираємо дані з відповіді сервера в dict, використовую метод `resp.json()`
created_issue = response.json()
print(response.status_code)
print(created_issue)

# оновлення імені нотатки, без зміни інших полів, використовуємо меод PATCH
new_data = {'name': 'Fixed name'}
response = requests.patch(issue_url(created_issue['id']),
                          data=json.dumps(new_data), headers=headers,
                          cookies=cookies)
print(response.status_code)
print(response.json())

# видалення нотатки з сервера з її `id`.
response = requests.delete(issue_url(created_issue['id']), cookies=cookies)
print(response.status_code)
# print(response.json())

# SESSION EXAMPLE
# Для більш простої схеми роботи та без постійної передачі cookies використовуємо механізм сесія в бібліотеці requests.
# cookies автоматично прокидаються при кожному запиті.

# авторизуємося і намагаємося виконати ті самі дії, але з request.Session.
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
# створюємо екземпляр `Session`
session = requests.Session()

response = session.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

# ми все також можемо взяти cookies із сесії (зробимо це для прикладу)
cookies = response.cookies

# виконуємо ті ж дії, але в рамках сесії.
# Сесія зберігатиме в собі cookies і оновлюватиме їх, якщо сервер їх змінить.
# А при кожному запиті в рамках екземпляра Session cookies будуть передаватися автоматично.

# отримуємо список нотаток
response = session.get(issues_url)
print(response.status_code)
print(response.json())

# створення нотатки з помилкою, що дані не були передані (error: ошибка данных - 400)
response = session.post(issues_url)
print(response.status_code)
print(response.json())

# POOL MANAGER збереження підключень та перевикористання їх
# pool_maxsize – максимальний розмір pool-а, за який не можна вийти.
# pool_block – блокуючий режим (True | False).
# pool_connections - кількість з'єднань, що кешуються.
# якщо pool_block == True - ми не зможемо вийти за межі maxsize і будемо змушені чекати, поки не звільниться сприяння
# (ми будемо як би в черзі на використання з'єднання з кешу)
# приклад:
# HTTPAdapter(pool_maxsize=100, pool_block=True, pool_connections=10)
# Максимальна кількість з'єднань 100, з блокуючим режимом та 10-ю з'єднаннями, що кешуються.
# Якщо кількість з'єднань буде 140, то 40 з них чекатиме в черзі, поки що якесь із 100 з'єднань не звільниться.

adapter = HTTPAdapter(pool_maxsize=10, pool_block=True, pool_connections=10)
session = requests.Session()
# для https кешируем соединения
session.mount('http://', adapter=adapter)
session.post(issues_url)
