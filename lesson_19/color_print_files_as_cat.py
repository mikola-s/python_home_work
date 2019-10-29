#!/usr/bin/env python
import print_files_as_cat


def color_print_files_as_cat(file_list=None):
    """ Выводит содержимое файлов  в терминал
    Использование: python3 print_file_as_cat.py [ПУТЬ]ФАЙЛ_1 [[ПУТЬ]ФАЙЛ_2 [ПУТЬ]ФАЙЛ_3 ...]

    Реализует программу cat в python 3.7.
    Выводит в терминал содержимое файла указанного в [ПУТЬ]ФАЙЛ
    [ПУТЬ]  может быть абсолютным или относительным
            можно не указывать если файл находится в текущей папке
    Если параметр [ПУТЬ]ФАЙЛ не указан не выводит ничего
    Если файл пустой то программа завершается.

    Пример:
    $ python3 print_file_as_cat.py example_files/example_file_1.txt example_files/example_file_2.py
    пример текстового файла
    для домашнего задания
    к уроку 19
    #пример файла python
    print('Мотурначка!')

    :param file_list:
    :return:

    """
    pass
