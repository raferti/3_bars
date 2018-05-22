import json
import math
import argparse


def load_data(file_path):
    try:
        with open(file_path, encoding='UTF8') as data_file:
            bars_data = json.load(data_file)
            return bars_data['features']
    except ValueError:
        exit('Данные в файле в неправильном формате')
    except FileNotFoundError:
        exit('.json файл с данными о барах не найден!')


def get_biggest_bar(bar_list):
    return max(bar_list,
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bar_list):
    return min(bar_list,
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_distance_to_bar(longitude, latitude, coordinates_x, coordinates_y):
    return math.sqrt((coordinates_x - longitude) ** 2 +
                     (coordinates_y - latitude) ** 2)


def get_name_bar(bar):
    return bar['properties']['Attributes']['Name']


def get_closest_bar(bar_list, longitude, latitude):
    try:
        return min(bar_list, key=lambda x: get_distance_to_bar(
            float(longitude),
            float(latitude),
            x['geometry']['coordinates'][0],
            x['geometry']['coordinates'][1]
            )
            )
    except ValueError:
        exit('Ошибка при расчете ближайшего бара. ' 
             'Значение координат должно быть числом')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str,
                        help='Путь и имя .json файла с параметрами баров')
    return parser


if __name__ == '__main__':
    script_argument = create_parser().parse_args()
    loaded_data = load_data(script_argument.file_path)
    longitude = input('Укажите долготу(longitude) '
                      'вашего местоположения (например 37.35807): ')
    latitude = input('Укажите широту(latitude)'
                     ' вашего местоположения (например: 55.846144): ')
    print('{} {}'.format('Самый большой бар',
                         get_name_bar(get_biggest_bar(loaded_data))))
    print('{} {}'.format('Самый маленький бар',
                         get_name_bar(get_smallest_bar(loaded_data))))
    print('{} {}'.format('Ближайший бар',
                         get_name_bar(
                             get_closest_bar(
                                 loaded_data,
                                 longitude,
                                 latitude
                             )
                         )
                         )
          )
