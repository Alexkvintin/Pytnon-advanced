from bs4 import BeautifulSoup
import requests
print('=' * 60)
city_def = 'киев'
city = input('Город: ')
city.lower()
if len(city) == 0:
    city = city_def
resp = requests.get(f'https://ua.sinoptik.ua/погода-{city}')
info = BeautifulSoup(resp.text, 'lxml')
# print(s)
if info.find("body", class_="ua p404"):
    print('Ошибка...\nНет искомой информации.')
else:
    date1 = []
    date2 = {}
    weather = (info.find("div", class_="tabs").text).split()
    city = (info.find("div", class_="cityName cityNameShort").text).split()
    # print(weather)
    for i in range(0, len(weather), 7):
        days = weather[0 + i:7 + i]
        # print(days)
        date2[days[1].lstrip('0')] = ' '.join(days)
        date1.append(days[1].lstrip('0'))
    print(*city)
    while True:
        input_date = input(f'Выберите дату с {date1[0]} по {date1[len(date1) - 1]}: ')
        try:
            print(date2[input_date])
        except KeyError:
            print('Некоректная дата!')
            if input('Другая дата (1-yes/enter-exit)') != '1':
                break
