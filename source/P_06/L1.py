def decorator(function):

    # Створюємо нову функцію
    def decorated_function():
        print("Код, що буде виконано до виклику функції")
        function()  # Виклик функції, що декорується
        print("Код, що буде виконано після виклику функції")

    # Повертаємо декоровану функцію
    return decorated_function

