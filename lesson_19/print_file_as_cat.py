#!/usr/bin/env python3
from sys import argv


def processing_write_str(write_str=None):
    if write_str == None:
        
    print(write_str)


def open_and_read_file(file_name=str):
    pass


def print_file_in_terminal(list_of_file=list):
    pass


def print_file_as_cat(file=str):
    """Выводит содержимое файла в терминал
    Использование: python3 print_file_as_cat.py [ПУТЬ]ФАЙЛ

    Реализует программу cat в python 3.7.
    Выводит в терминал содержимое файла указанного в [ПУТЬ]ФАЙЛ
    [ПУТЬ]  может быть абсолютным или относительным
            можно не указывать если файл находится в текущей папке
    Если параметр [ПУТЬ]ФАЙЛ не указан catch
    Если файл пустой то программа завершается.

    Пример:
    $ python3 print_file_as_cat.py example_files/example_file_1.txt

    пример
    текстового
    файла
    для
    домашнего задания
    к уроку 19

    :param file: [путь_к_файлу]имя_файла
    :return: None

    """
    print_file_in_terminal(open_and_read_file(processing_write_str(argv[1])))


print_file_as_cat()
