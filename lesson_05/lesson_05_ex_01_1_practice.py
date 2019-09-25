# Задание 1
# Написать 2 функции.
# Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк.
# Отдельно каждую функцию к отдельному списку строк!

def to_lower(string):
    return string.lower()


def to_upper(string):
    return string.upper()


for_to_lower = """One Night the BIG BAD WOLF,
                who dearly loved to eat fat
                little piggies, came along
                and saw the first little pig
                in his house of straw.""".split()

for_to_upper = """He said "Let me in, Let me in,
                little pig or I'll huff and I'll
                puff and I'll blow your house in!"
                "Not by the hair of my chinny chin chin",
                said the little pig. But of course the
                wolf did blow the house in and ate the
                first little pig.""".split()

print(list(map(to_lower, for_to_lower)), '\n')

print(list(map(to_upper, for_to_upper)))
