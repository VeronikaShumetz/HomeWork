# форматирование через f-string
# name = 'Veronika'
# age = 27
# print(f'Привет,{name}!\nТебе уже {age} лет!')
#
# # через %
# name = 'Veronika'
# age = 27
# print('Привет,%s!\nТебе уже %d лет!' % (name, age))
#
# # через str.format()
# name = 'Veronika'
# age = 27
# print('Привет,{}!\nТебе уже {} лет!'.format(name, age))
#
# a=1
# b=2
# c=3
# print(f'четное:{b=},нечетное:{a=}')

#Homework4

name = (input('Введите свое имя: ').title())
age = int(input('Введи свой возраст: '))
massage = ''

if not name:
    massage = (f'Ты не ввел имя. Введи имя')
elif len(name) < 3:
    massage = (f'{name},ошибка.Имя меньше 3 символов')

if age <= 0:
    massage = (f'Ошибка. Слишком низки возраст')
elif age < 14:
    massage = (f'{name}, ты слишком мал(-a)!')

if not massage:
    massage = (f'Привет,{name}. Тебе {age} лет')
    if 16 <= age <= 17:
        massage = (f'Привет,{name}! Получи свой 1ый паспорт')
    elif 25 <= age <= 27:
        massage = (f'Привет,{name}!Обнови свой паспорт')
    elif 45 <= age <= 46:
        massage = (f'Привет,{name}!Обнови свой паспорт!')

print(massage)