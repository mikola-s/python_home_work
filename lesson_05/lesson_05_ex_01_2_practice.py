##Задание 2
##Написать функцию которая будет простое число возводить в квардрат.
##Необходимо возвести в квадрат все простые числа в списке используя
##функцию map

from random import randint

start_list = [randint(1,100) for num in range(20)]
print(start_list)

def simple_square(num):
    for divider in range(2, num):
        if num % divider == 0:
            return num
    return num*num
    
print(list(map(simple_square, start_list)))



