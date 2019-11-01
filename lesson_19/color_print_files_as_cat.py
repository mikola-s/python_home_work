#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pygments import highlight  # Pygments version 2.4.2
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers import guess_lexer_for_filename
from print_file_as_cat import open_and_read_file
from print_file_as_cat import processing_input


def print_colored_file(file_path, file_list):
    """    выводит содержимое файла, раскрашенное соответственно типу файла и коду в файле, в стандартный вывод

    :param file_path: [<ПУТЬ>]<ФАЙЛ>
    :param file_list: <список со строками файла>

    """
    code = ''.join(file_list)
    print(highlight(code, guess_lexer_for_filename(file_path, code), Terminal256Formatter()), end='')


def color_print_files_as_cat(files_list):
    """   Выводит содержимое одного или нескольких файлов в стандартный вывод
    раскрашенное соответственно типу файла и коду в файле

    Применение:
    $ python3 print_files_as_cat.py [<ПУТЬ>]<ФАЙЛ> [[<ПУТЬ>]<ФАЙЛ> ...]

    Дополнительная информация: <https://github.com/mikola-s/python_home_work/tree/master/lesson_19>

    """
    temp_var = [print_colored_file(file, open_and_read_file(processing_input(file))) for file in files_list]


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv.count('--help') == 0:
        color_print_files_as_cat(sys.argv[1::])
    else:
        print(color_print_files_as_cat.__doc__)
