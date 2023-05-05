# личные данные
my_name = 'Вячеслав'
my_surname = 'Костров'
my_job_title = 'Инженер-тестировщик'
my_work_experience = '9 лет 4 месяца'
my_resume = 'По гороскопу - скорпион. Я в своем познании настолько преисполнился, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля'
my_fullname = my_surname, my_name

# текст для прилюдии
welcome_message = 'Привет, меня зовут'
work_message = 'Моя должность:'
work_experience_message = 'Стаж работы:'

# вывод сообщения
print(welcome_message, my_surname, my_name)
print(work_message, my_job_title)
print(work_experience_message, my_work_experience)
print('О себе:', my_resume)

# пример по вопросу 1
print(welcome_message, my_surname, my_name, work_message, my_job_title, work_experience_message, my_work_experience, 'О себе:', my_resume)

# пример по вопросу 2
print(my_fullname)