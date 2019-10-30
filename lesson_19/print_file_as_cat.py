#!/usr/bin/env python3
import sys
import os


def processing_input(input_str):
    """ проверяет введенный путь и имя файла

    проверяет есть ли в path_file путь и является ли он путем к файлу
    если файл не существует или путь неправильный возвращает сообщение об ошибке

    :param input_str: <строка содержащая путь и имя файла>
    :return <путь и имя файла>

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

    print('введите ./print_file_as_cat.py --help, чтобы получить дополнительную информацию\n')
    sys.exit()


def open_and_read_file(path_file):
    """
    открывает файл на чтение и считывает его построчно в список

    :param path_file: строка содержащая [<путь к файлу>]<имя файла>
    :return: список со строками файла

    """
    try:
        with open(path_file) as incoming_file:
            return [line for line in incoming_file]
    except IOError:
        print('IOError не удалось обработать файл --', path_file)


def print_file(list_of_file):
    """
    выводит элементы списка в терминал

    :param list_of_file: список содержащий строки заданного файла

    """
    return [print(line, end='') for line in list_of_file]


def print_file_as_cat(argument=str):
    """
    Выводит содержимое файла в терминал

    Использование:  $ python3 print_file_as_cat.py [<пусть к файлу>]<имя файла>
              или   $ ./print_file_as_cat.py [<путь к файлу>]<имя файла>

    Реализует программу cat в python 3.7.
    Выводит в терминал содержимое файла с именем указанным в [<путь к файлу>]<имя файла>

    :param argument: [<путь к файлу>]<имя файла>

    Если в [<путь к файлу>]<имя файла> есть пробелы их надо писать в кавычках (")
    Пример: "c:/Program Files/test.txt" "/home/dir with space/file name with space.txt"

    <путь к файлу>  может быть абсолютным или относительным
                    можно не указывать если файл находится в текущей папке

    Если параметр [<путь к файлу>]<имя файла> не указан выводит print_file_as_cat.__doc__

    Примеры использования:
    $ python3 print_file_as_cat.py example_files/example_file_1.txt
    пример текстового файла
    для домашнего задания
    к уроку 19

    $ ./print_file_as_cat.py example_files/example_file_2.py
    #пример файла python
    print('Мотурначка!')

    """

    print_file(open_and_read_file(processing_input(argument)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_file_as_cat(sys.argv[1])
    else:  # если аргументы не переданы
        print('\nвведите ./print_file_as_cat.py --help, чтобы дополнительную информацию\n')
