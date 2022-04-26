# name = (input('Введите свое имя: ').title())
# age = int(input('Введи свой возраст: '))
# massage = ''

def main():
    name = (input('Введите свое имя: ').title())
    age = int(input('Введи свой возраст: '))

    def valid_name(name: str) -> str:
        """Валидация имени"""
        if not name:
            return f'Ты не ввел имя. Введи имя'
        if len(name) < 3:
            return f'{name},ошибка.Имя меньше 3 символов'
        if name.strip().count('')==1:
            return

        return ''

    def valid_age(age: int) -> int:
        """Валидация возраста"""
        if age <= 0:
            return f'Ошибка. Слишком низки возраст'
        if age < 14:
            return f'{name}, ты слишком мал(-a)!'

        return ''

    def advice_massage (massage: str) -> str:
        """Доп. сообщения"""
        if not massage:
            return ''
        if 16 <= age <= 17:
            return f'Привет,{name}! Получи свой 1ый паспорт'
        elif 25 <= age <= 27:
            return f'Привет,{name}!Обнови свой паспорт'
        elif 45 <= age <= 46:
            return f'Привет,{name}!Обнови свой паспорт!'

print(main())