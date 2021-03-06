# generate file input_data_file_for_fizz_buzz.txt
# for working file lesson_03_ex_02_fizz_buzz.py
#         and file lesson_03_ex_03_fizz_buzz.py

from os import linesep
from random import randint

with open('input_data_file_for_fizz_buzz.txt', 'w') as data_file:
    for counter in range(20):
        fizz = randint(2, 10)
        buzz = fizz + randint(1, 10)
        end_number = randint(buzz, 100)
        data_file.write(str(fizz) + ' ' + str(buzz) + ' ' + str(end_number))
        data_file.write(linesep if counter != 19 else '')
