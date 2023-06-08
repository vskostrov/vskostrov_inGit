# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код

import random
import string

def generate_random_name():
    """
    Генератор который генерирует два слова из латинских букв (верхнего и нижнего регистра) от 1 до 15 символов, разделенных пробелами.
    :return: Строка из двух случайных латинских слов от 1 до 15 символов, которые разделенны между собой пробелом.
    """
    while True:
        letters = string.ascii_letters # Алфавит из латинских букв из набора ASCII в верхнем и нижнем регистрах.
        word1 = "".join(random.choice(letters) for i in range(random.randint(1, 15)))
        word2 = "".join(random.choice(letters) for i in range(random.randint(1, 15)))
        words = str(word1 + " " + word2)
        yield words

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))