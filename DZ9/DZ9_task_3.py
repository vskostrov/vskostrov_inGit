# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path #Уж очень мне нравится указывать пути так
task_3_txt = Path("test_file/task_3.txt") #Уж очень мне нравится указывать пути так

with open(task_3_txt, mode='r') as file:
    x = 0
    list_sum = []
    for one_line in file.readlines():
        if len(one_line) > 2:
            x += int(one_line[:-1])
        else:
            list_sum.append(x)
            x = 0
list_sum = sorted(list_sum)[-3:]
three_most_expensive_purchases = sum(list_sum)

assert three_most_expensive_purchases == 202346
