import json
import math


def load_data(file_path='bars.json'):
    with open(file_path, encoding='UTF8') as data_file:
        bars_data = json.load(data_file)
        return bars_data['features']


def get_biggest_bar(bar_list):
    return max(bar_list, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bar_list):
    return min(bar_list, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_distance_to_bar(longitude, latitude, coordinates_x, coordinates_y):
    return math.sqrt((coordinates_x - longitude) ** 2 + (coordinates_y - latitude) ** 2)


def get_name_bar(bar):
    bar_name = 'носит название: {}'
    return bar_name.format(bar['properties']['Attributes']['Name'])


def get_closest_bar(bar_list, longitude, latitude):
    try:
        longitude = float(longitude)
    except ValueError:
        exit('Долгота(longitude) должна быть числом')

    try:
        latitude = float(latitude)
    except ValueError:
        exit('Широта(latitude) должна быть числом')

    return min(
        bar_list,
        key=lambda x:
        get_distance_to_bar(
                            longitude,
                            latitude,
                            x['geometry']['coordinates'][0],
                            x['geometry']['coordinates'][1]
                        )
        )


if __name__ == '__main__':
    try:
        loaded_data = load_data()
    except FileNotFoundError:
        exit('Файл bars.json не найден!')

    longitude = input('Укажите долготу(longitude) вашего местоположения (например 37.35805): ')
    latitude = input('Укажите широту(latitude) вашего местоположения (например: 55.846144): ')

    print('{} {}'.format('Самый большой бар', get_name_bar(get_biggest_bar(loaded_data))))
    print('{} {}'.format('Самый маленький бар', get_name_bar(get_smallest_bar(loaded_data))))
    print('{} {}'.format('Ближайший бар', get_name_bar(get_closest_bar(loaded_data, longitude, latitude))))
