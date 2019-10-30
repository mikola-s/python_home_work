#!/usr/bin/env python3
import sys
import os


def processing_input(path_file=str):
    """ проверяет введенный путь и имя файла

    проверяет есть ли в path_file путь и является ли он путем к файлу
    если файл не существует или путь неправильный возвращает сообщение об ошибке

    :param path_file: <строка содержащая путь и имя файла>
    :return <путь и имя файла>

    """

    if os.path.exists(path_file):
        return path_file if os.path.isfile(path_file) \
            else print('\nОшибка:', path_file, '-- не являеться файлом\n')
    else:
        print('\nОшибка:', path_file, '-- неверный путь\n')


# if os.path.isfile(path_file):
#     return path_file
# else:
#     return print('\nОшибка:', path_file, '-- не являеться файлом\n')

def open_and_read_file(path_file=str):
    """
    открывает файл на чтение и считывает его построчно в список

    :param path_file: строка содержащая путь к файлу и имя файл
    :return: список с данными файла

    """
    pass


def print_file_in_terminal(list_of_file=list):
    """
    выводит элементы списка в терминал

    :param list_of_file: список

    """
    temp = [print(line) for line in list_of_file]


def print_file_as_cat(path_file):
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

    :param path_file: [<путь к файлу>]<имя файла>
    :return:

    """
    return processing_input(path_file) if path_file else False

    # print_file_in_terminal(open_and_read_file(processing_input(path_file)))


if __name__ == "__main__":
    path_file = './example_files'
    # path_file = './color_print_files_as_cat.py'
    # path_file = ''
    # path_file = None

    # processing_input(path_file)
    print_file_as_cat(path_file)
    # print_file_as_cat(sys.argv[1])
