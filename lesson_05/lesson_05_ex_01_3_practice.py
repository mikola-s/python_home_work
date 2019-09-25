##Задание 3
##Вспоминаем работу с файлом. Есть файл, в котором много
##англоязычных текстовых строк. Считаем частоту встретившихся
##слов в файле, но через функции и map, без единого цикла!

from re import sub

def cleaner(string):
    return sub(r"[^\w']", "", string)

def counter(item):
    rezult_dict[item] += 1

def printing(item):
    print(rezult_dict[item], '\t', item)
    

with open('text_for_ex_01_3_practice.txt', 'r') as story:
    story_list = list(map(cleaner, story.read().split()))

rezult_dict = dict.fromkeys(list(set(story_list)), 0)

temp = list(map(counter, story_list))

temp = list(map(printing, sorted(rezult_dict.keys())))
