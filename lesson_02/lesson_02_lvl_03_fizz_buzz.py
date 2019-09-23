##Домашнее задание урок 2. Третий уровень ("Мистер Буль. Джордж Буль!"):
##Решить задачу:
##Задача fizz-buzz:
##У вас есть три числа, они вводятся из консоли.
##Первое число называется fizz, второе называется buzz.
##До третьего необходимо досчитать от единицы.
##Считая, надо выводить число.
##Если число кратно fizz - надо выводить F вместо числа.
##Если число кратно buzz - надо выводить B вместо числа.
##Если число кратно и fizz и buzz, надо выводить FB.
##И так - пока не будет достигнуто третье введенное число.
##Пример условия и результата:
##Введены числа 2, 5, 18
##Вывод должен быть таким:
##1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F


print('enter number Fizz')
fizz = int(input())

print ('enter number Buzz')
buzz = int(input())

print('enter end number')
end_number = int(input())

rezult = ''

if end_number > fizz and end_number > buzz:
    for counter in range(1, end_number + 1):
        if counter % fizz == 0 and counter % buzz == 0:
            rezult += ' FB'
        elif counter % fizz == 0:
            rezult += ' F'
        elif counter % buzz == 0:
            rezult += ' B'
        else:
            rezult += ' ' + str(counter)

print(rezult)

