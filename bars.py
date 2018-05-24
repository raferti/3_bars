import json
import math
import argparse


def load_data(file_path):
    try:
        with open(file_path, encoding='UTF8') as data_file:
            bars_data = json.load(data_file)
            return bars_data['features']
    except ValueError:
        return None


def get_biggest_bar(bar_list):
    return max(
        bar_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bar_list):
    return min(
        bar_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_distance_to_bar(longitude, latitude, coordinates_x, coordinates_y):
    return math.sqrt((coordinates_x - longitude) ** 2 +
                     (coordinates_y - latitude) ** 2)


def get_name_bar(bar):
    return bar['properties']['Attributes']['Name']


def get_closest_bar(bar_list, longitude, latitude):
    closest_bar = min(
        bar_list,
        key=lambda x: get_distance_to_bar(
            float(longitude),
            float(latitude),
            x['geometry']['coordinates'][0],
            x['geometry']['coordinates'][1]
        )
    )
    return closest_bar


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str,
                        help='Путь и имя .json файла с параметрами баров')
    return parser


def is_float_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    script_argument = create_parser().parse_args()
    try:
        loaded_data = load_data(script_argument.file_path)
        if loaded_data is None:
            error = 'Данные в файле в неправильном формате'
            raise ValueError(error)
    except FileNotFoundError:
        error = '.json файл с данными о барах не найден!'
        raise FileNotFoundError(error)

    longitude = input('Укажите долготу(longitude) '
                      'вашего местоположения (например 37.35807): ')
    latitude = input('Укажите широту(latitude)' 
                     ' вашего местоположения (например: 55.846144): ')

    if is_float_number(longitude) and is_float_number(latitude):
        pass
    else:
        raise ValueError('Ошибка расчета ближайшего бара. '
                         'Значение координат должно быть числом')

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

