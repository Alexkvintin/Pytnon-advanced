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
    num_of_days = []
    new_day_dict = {}
    weather = (info.find("div", class_="tabs").text).split()
    city = (info.find("div", class_="cityName cityNameShort").text).split()
    # print(weather)
    for i in range(0, len(weather), 7):
        days = weather[0 + i:i + 7]
        new_day_dict[days[1]] = ' '.join(days)
        num_of_days.append(days[1])
    # print(*city)
    while True:
        day_num = input(f'Выберите дату с {num_of_days[0]} по {num_of_days[-1]}: ')
        try:
            print(new_day_dict[day_num])
        except KeyError:
            print('Некоректная дата!')
        switch = input('Другая дата (1-yes/enter-exit)')
        if switch != '1':
            break
print('='*60)
