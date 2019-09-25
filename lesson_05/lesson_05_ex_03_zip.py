# Разбираемся, что делает функция zip, и пробуем #написать свой собственный zip.

from random import randint, choice


def fill_list(list_size):
    return [randint(0, 100) for elem in range(list_size)]


elem_in_list = randint(3, 9)

first_elem_list = fill_list(elem_in_list)
second_elem_list = fill_list(elem_in_list)

with open('text_for_ex_01_3_practice.txt', 'r') as file_for_list:
    list_for_choice = file_for_list.read().split()

third_elem_list = [choice(list_for_choice) for elem in range(elem_in_list)]

print('\nstart lists')
print(first_elem_list)
print(second_elem_list)
print(third_elem_list, '\n')

zip_list = list(zip(first_elem_list, second_elem_list, third_elem_list))
zip_dict = dict(zip(third_elem_list, zip(first_elem_list, second_elem_list)))

print('zip list \n', zip_list, '\n')
print('zip dict \n', zip_dict, '\n')

temp = [print(zip_list_line) for zip_list_line in zip_list]
