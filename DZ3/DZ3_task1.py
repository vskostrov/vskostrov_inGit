# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def modification(lst):
    # Здесь пишем код
    first_symbol = lst.pop(0) #получили первый символ по индексу и удалили
    last_symbol = lst.pop() #получили последний символ по индексу и удалили (индекс -1 не пишем, там и так последний по-умолчанию)
    lst.insert(0, last_symbol) #вставляем последним символом первый символ (что определили попом)
    lst.append(first_symbol) #просто добавляем первый символ последним
    return lst


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
