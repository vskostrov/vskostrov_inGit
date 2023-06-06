# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path
import re

read_file = Path("test_file/task1_data.txt")
write_file = Path("test_file/task1_answer.txt")

with open(read_file, mode='r', encoding='utf-8') as file1:
    with open(write_file, mode='w', encoding='utf-8') as file2:
        file_content = file1.readlines()
        file2.writelines(re.sub('[0-9]', '', file_line) for file_line in file_content)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
