##Задание 3
##Вспоминаем работу с файлом. Есть файл, в котором много
##англоязычных текстовых строк. Считаем частоту встретившихся
##слов в файле, но через функции и map, без единого цикла!

with open('text_for_ex_01_3_practice.txt', 'r') as story:
    story_list = story.read().split()

rezult_dict = dict.fromkeys(list(set(story_list)), 0)

def counter(item):
    rezult_dict[item] += 1

temp = list(map(counter, story_list))

print(rezult_dict)
