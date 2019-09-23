##Домашнее задение урок 3. Задание 3.
##Переделать вторую задачу так, чтобы результат писался в другой файл.

from os import linesep

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
    return ('fizz = ' + str(fizz) + '  buzz = ' + str(buzz) + 
           '  end number = '+ str(end_number) + linesep + 
           str(rezult) + linesep + linesep)
    
with open('./data_file_for_fizz_buzz.txt', 'r') as data_file:
    for_save_in_file = ''
    for line in data_file:
        fizz_buzz_list = list(map(int, line.split()))
        for_save_in_file += fizz_buzz(fizz_buzz_list[0],
                                      fizz_buzz_list[1],
                                      fizz_buzz_list[2])
print(for_save_in_file)
with open('./rezult_lssn_03_ex_03.txt', 'w') as file_for_save:
    file_for_save.write(for_save_in_file)
