from urllib import request

# отримуємо вміст сторінки по domain- як порт буде використаний 80
# # Для вказівки іншого порту використовуємо запис виду: http://example:81.com
response = request.urlopen('http://example.com')

# друкуємо інформацію про http-відповідь
print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# отримуємо заголовки у вигляді внутрішнього об'єкта
print(response.headers)
# отримуємо словник усіх заголовків
print(response.getheaders())
# отримання заголовку
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))

print(response.headers.get('Expires'))
print(response.getheader('Expires'))
