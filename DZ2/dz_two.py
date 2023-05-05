import math #подключение math.sqrt() для корня
# задание 1
print("Задание 1")
side_square = 2  #сторона квадрата
P_square = side_square * 4   #периметр квадрата
S_square = pow(side_square, 2) #площадь квадрата "pow - возводит число в степень"
D_square = side_square * math.sqrt(2) #диагональ квадрата math.sqrt(2) даёт квадратный корень из 2

# задание 1
print("Периметр квадрата:", P_square)
print("Площадь квадрата:", S_square)
print("Диагональ квадрата:", D_square)
print("\t") # Для красоты пустая строка

# задание 2
print("Задание 2")
a = 10
b = 20
c = 3
D = (b**2) - (4 * a * c) # Вычисление дискриминанта
if D > 0: # Проверка, что дискриминант больше 0
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Корни:", round(x1, 2), "и", round(x2, 2))
else:
    print("Корней нет")
print("\t") # Для красоты пустая строка

print("Задание 3")
string1 = "Сладкие булочки"
string2 = "Солёные пирожки"
change1 = string2[:2] + string1[2:]
change2 = string1[:2] + string2[2:]
print(change1, change2)
print("\t") # Для красоты пустая строка

print("Задание 4")
file= r'C:\Users\vs.kostrov\секрет.txt'
file_name = file.split('\\')[-1].split('.')[0]
drive = file.split(':')[0]
folder = file.split('\\')[1].split(':')[0]
print("Имеем путь к файлу:", file)
print("Имя файла:", file_name)
print("Диск:", drive)
print("Корневая папка:", folder)
print("\t") # Для красоты пустая строка

print("Задание 5")
a = 5
b = 16
sum = '{} + {} = {}' .format(a, b, a+b)
multiplication = '{} * {} = {}'.format(a, b, a*b)
print("Сумма:", sum)
print("Произведение:", multiplication)
print("\t") # Для красоты пустая строка

print("Задание 6")
string = "Валентинки - это люди, а не сердечки из бумаги!"
modification_string = string[1::2]
print("Дана строка:", string)
print("Строка без нечетных индексов:", modification_string)
print("\t") # Для красоты пустая строка

print("Задание 7")
string1 = "wtf"
string2 = "brick quz jmpy veldt whangs fox"
index = string2.find(string1[0]), string2.find(string1[1]), string2.find(string1[2]) # ищем индексы символов из первой строки во второй
slice_min = string2[min(index):max(index) +1] # +1 выглядит как костыль(( но другого решения не нашел(
print("Срез минимальной длины:", slice_min)