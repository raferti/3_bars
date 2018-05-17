import json
import math


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF8') as data_file:
        bars_data = json.load(data_file)
        return bars_data


def get_biggest_bar(data):
    seats_count = 0
    name = 'ничего не найдено'
    for i in range(len(data['features'])):
        if seats_count < data['features'][i]['properties']['Attributes']['SeatsCount']:
            seats_count = data['features'][i]['properties']['Attributes']['SeatsCount']
            name = data['features'][i]['properties']['Attributes']['Name']
    return name


def get_smallest_bar(data):
    seats_count = 0
    name = 'ничего не найдено'
    for i in range(len(data['features'])):
        if seats_count >= data['features'][i]['properties']['Attributes']['SeatsCount']:
            seats_count = data['features'][i]['properties']['Attributes']['SeatsCount']
            name = data['features'][i]['properties']['Attributes']['Name']
    return name


def get_closest_bar(data, longitude, latitude):
    dist = 0.0
    name = 'ничего не найдено'
    for i in range(len(data['features'])):
        if dist >= math.sqrt((data['features'][i]['geometry']['coordinates'][0] - longitude) ** 2 +
                                             (data['features'][i]['geometry']['coordinates'][1] - latitude) ** 2):
            name = data['features'][i]['properties']['Attributes']['Name']
    return name


if __name__ == '__main__':
    filepach = input('Укажите путь и имя .json файла:  ')
    try:
        data_loading = load_data(filepach)
    except FileNotFoundError:
        print("Файл не найден!")
        exit()

    longitude = float(input('Укажите долготу(longitude) вашего местоположения: '))
    latitude = float(input('Укажите широту(latitude) вашего местоположения: '))

    print('Самый большой бар: ' + get_biggest_bar(data_loading))
    print('Самый маленький бар: ' + get_smallest_bar(data_loading))
    print('Ближайший бар: ' + get_closest_bar(data_loading, longitude, latitude))
