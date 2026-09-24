from analyser import *

request = input('Чим я можу вам допомогти? ')
while request != 'off':
    analyse(request)
    request = input('Чим я вам ще можу допомогти? (off - завершити): ')
