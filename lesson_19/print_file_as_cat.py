#!/usr/bin/env python3
import os
import sys


def processing_input(input_str):
    """
    проверяет введенный путь и имя файла

    проверяет есть ли в input_str путь и является ли он путем к файлу
    если файл не существует или путь неправильный возвращает сообщение об ошибке
    :param input_str: [<ПУТЬ>]<ФАЙЛ>
    :return: [<ПУТЬ>]<ФАЙЛ>
    """

    if os.path.exists(input_str):
        if os.path.isfile(input_str):
            return input_str
        else:
            print('\nОшибка:', input_str, '-- не являеться файлом\n')
    elif input_str == '--help':
        print(print_file_as_cat.__doc__)
    else:
        print('\nОшибка:', input_str, '-- неверный путь\n')
    print('запустите программу с атрибутом --help чтобы получить дополнительную информацию')
    sys.exit()


def open_and_read_file(path_file):
    """
    открывает файл на чтение и считывает его построчно в список

    :param path_file: [<ПУТЬ>]<ФАЙЛ>
    :return: <список со строками файла>
    """
    try:
        with open(path_file) as incoming_file:
            return [line for line in incoming_file]
    except IOError:
        print('IOError: не удалось обработать файл --', path_file)


def print_file(list_of_file):
    """
    выводит элементы списка в стандартный вывод

    :param list_of_file: <список>
    """
    return [print(line, end='') for line in list_of_file]


def print_file_as_cat(argument=str):
    """
    Выводит содержимое файла в стандартный вывод

    Применение: ~$ python3 print_file_as_cat.py [<ПУТЬ>]<ФАЙЛ>
                ~$ ./print_file_as_cat.py [<ПУТЬ>]<ФАЙЛ>

    Дополнительная информация: <https://github.com/mikola-s/python_home_work/tree/master/lesson_19>
    """

    print_file(open_and_read_file(processing_input(argument)))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv.count('--help') == 0:
        print_file_as_cat(sys.argv[1])
    else:
        print(print_file_as_cat.__doc__)
