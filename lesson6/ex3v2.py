import json
import urllib.request
import datetime

nap = ['С', 'ССВ', 'СВ', 'ВСВ', 'В', 'ВЮВ', 'ЮВ', 'ЮЮВ', 'Ю', 'ЮЮЗ', 'ЮЗ', 'ЗЮЗ', 'З', 'ЗСЗ', 'СЗ', 'ССЗ']
delta_phi = 22.5


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%H:%m')
    return converted_time


def url_builder(city_id):
    user_api = 'e551ef6a844d751ce13346b65180e670'
    unit = 'metric'
    api = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}'
    full_api_url = api + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        # time=,
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('wind').get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def get_dir(d):
    d += delta_phi / 2
    if d > 360:
        d -= 360
    index = (d / delta_phi)
    return nap[int(index)]


def data_output(data):
    degr = '\xb0' + 'C'

    print('='*60)
    print('')
    print('Погода сейчас в: {}, {}:'.format(data['city'], data['country']))
    # print('Время {}'.format((data['time'])))
    if data['sky'] == "Clouds":
        sky = "Облачно"
    if data['sky'] == "Mist":
        sky = "Туман"
    if data['sky'] == "Rain":
        sky = "Дождь"
    if data['sky'] == "Drizzle":
        sky = "Изморось"
    if data['sky'] == "Clear":
        sky = "Ясно"
    if data['sky'] == "Snow":
        sky = "Снег"
    print("Температура: {} {}. {}.".format(data['temp'], degr, sky))
    print('')
    print('Изменение температуры в ближайшее время: от {} до {} °C'.format(data['temp_min'], data['temp_max']))
    print('')
    print(f'Направление ветра: {get_dir(data["wind_deg"])}')
    print('Скорость ветра: {} м/c'.format(data['wind']))

    print('Относительная влажность: {} %'.format(data['humidity']))
    print('Плотность облаков: {} %'.format(data['cloudiness']))
    a = data['pressure'] / 1.3332239
    b = round(a)
    print('Давление: ' + str(b) + ' мм рт.ст.')
    print('Восход: {}'.format(data['sunrise']))
    print('Закат: {}'.format(data['sunset']))
    print('')
    print('Последнее обновление: {}'.format(data['dt']))
    print('='*60)


if __name__ == '__main__':
    try:
        data_output(data_organizer(data_fetch(url_builder(703448))))
    except IOError:
        print('no internet')
