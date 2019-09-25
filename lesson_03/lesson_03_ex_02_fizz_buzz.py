# Домашнее задение урок 3. Задание 2.
# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите.

def fizz_buzz(fizz, buzz, end_number):
    rezult = ''
    for counter in range(1, end_number + 1):
        if counter % fizz == 0 and counter % buzz == 0:
            rezult += ' FB'
        elif counter % fizz == 0:
            rezult += ' F'
        elif counter % buzz == 0:
            rezult += ' B'
        else:
            rezult += ' ' + str(counter)
    print('fizz =', fizz, ' buzz =', buzz, ' end number =', end_number)
    print(rezult, '\n')


with open('./input_data_file_for_fizz_buzz.txt', 'r') as data_file:
    for line in data_file:
        fizz_buzz_list = list(map(int, line.split()))
        fizz_buzz(fizz_buzz_list[0], fizz_buzz_list[1], fizz_buzz_list[2])
