#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from print_file_as_cat import print_file_as_cat as print_one_file


def print_files_as_cat(files_list):
    """    Выводит содержимое одного или нескольких файлов в стандартный вывод

    Применение: $ python3 print_files_as_cat.py [<ПУТЬ>]<ФАЙЛ> [[<ПУТЬ>]<ФАЙЛ> ...]

    Дополнительная информация: <https://github.com/mikola-s/python_home_work/tree/master/lesson_19>
    """

    temp_var = [print_one_file(file) for file in files_list]
    # temp = map(print_one_file, file_list)  # map почему-то не завелся


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv.count('--help') == 0:
        print_files_as_cat(sys.argv[1::])
    else:
        print(print_files_as_cat.__doc__)
