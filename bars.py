import json
import math


def load_data(filepath):
    with open(filepath, encoding='UTF8') as data_file:
        bars_data = json.load(data_file)
        return bars_data


def get_biggest_bar(bar_list):
    return max(bar_list['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bar_list):
    return min(bar_list['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_distance_to_bar(longitude, latitude, coordinates_x, coordinates_y):
    return math.sqrt((coordinates_x - longitude) ** 2 + (coordinates_y - latitude) ** 2)


def get_closest_bar(bar_list, longitude, latitude):
    return min(bar_list['features'], key=lambda x: get_distance_to_bar(longitude, latitude,
                                                                       x['geometry']['coordinates'][0],
                                                                       x['geometry']['coordinates'][1]))


if __name__ == '__main__':

    file_pach = input('Укажите путь и имя .json файла:  ')
    try:
        data_loading = load_data(file_pach)
    except FileNotFoundError:
        print("Файл не найден!")
        exit()

    longitude = float(input('Укажите долготу(longitude) вашего местоположения: '))
    latitude = float(input('Укажите широту(latitude) вашего местоположения: '))

    print('Самый большой бар: ' + str(get_biggest_bar(data_loading)))
    print('Самый маленький бар: ' + str(get_smallest_bar(data_loading)))
    print('Ближайший бар: ' + str(get_closest_bar(data_loading, longitude, latitude)))
