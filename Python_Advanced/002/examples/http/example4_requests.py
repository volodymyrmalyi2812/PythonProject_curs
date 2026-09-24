import requests

# pip install requests
# запускаємо різні види запитів, але вже з використанням бібліотеки requests
response1 = requests.get('https://forumodua.com/showthread.php?t=3308785')
response2 = requests.put('https://forumodua.com/showthread.php?t=3308785')
response3 = requests.post('https://forumodua.com/showthread.php?t=3308785')
response4 = requests.delete('https://forumodua.com/showthread.php?t=3308785')
print(response1)
print(response2)
print(response3)
print(response4)
