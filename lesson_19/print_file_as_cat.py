#!/usr/bin/env python3
import sys
import os


def processing_input(input_str=str):
    """ проверяет введенный путь и имя файла

    проверяет есть ли в path_file путь и является ли он путем к файлу
    если файл не существует или путь неправильный возвращает сообщение об ошибке

    :param input_str: <строка содержащая путь и имя файла>
    :return <путь и имя файла>

    """

    if os.path.exists(input_str):
        return input_str if os.path.isfile(input_str) else print('\nОшибка:', input_str, '-- не являеться файлом\n')
    else:
        print('\nОшибка:', input_str, '-- неверный путь\n')


def open_and_read_file(path_file=str):
    """
    открывает файл на чтение и считывает его построчно в список

    :param path_file: строка содержащая путь к файлу и имя файла
    :return: список со строками файла

    """
    try:
        with open(path_file) as incoming_file:
            return [line for line in incoming_file]
    except IOError:
        print('IOError не удалось обработать файл --', path_file)


def print_file_in_terminal(list_of_file=list):
    """
    выводит элементы списка в терминал

    :param list_of_file: список

    """
    return [print(line) for line in list_of_file]


def print_file_as_cat(argument):
    """Выводит содержимое файла в терминал

    Использование:  $ python3 print_file_as_cat.py [<пусть к файлу>]<имя файла>
              или   $ ./print_file_as_cat.py [<путь к файлу>]<имя файла>

    Реализует программу cat в python 3.7.
    Выводит в терминал содержимое файла с именем указанным в [<путь к файлу>]<имя файла>
    Если в [<путь к файлу>]<имя файла> есть пробелы их надо писать в кавычках (")
    Пример: "c:/Program Files/test.txt" "/home/dir with space/file name with space.txt"

    <путь к файлу>  может быть абсолютным или относительным
                    можно не указывать если файл находится в текущей папке

    Если параметр [<путь к файлу>]<имя файла> не указан catch

    Если аргументы не передаются программа ничего не выводит

    Примеры использования:
    $ python3 print_file_as_cat.py example_files/example_file_1.txt
    пример текстового файла
    для домашнего задания
    к уроку 19

    $ ./print_file_as_cat.py example_files/example_file_2.py
    #пример файла python
    print('Мотурначка!')

    :param argument: [<путь к файлу>]<имя файла>
    :return:

    """
    return open_and_read_file(processing_input(argument)) if argument else False


if __name__ == "__main__":
    path_file = './example_files/example_file_1.txt'
    # path_file = './color_print_files_as_cat.py'
    # path_file = ''
    # path_file = None

    # processing_input(path_file)
    print_file_as_cat(path_file)
    # print_file_as_cat(sys.argv[1])
