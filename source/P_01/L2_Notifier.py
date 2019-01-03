class Notifier:
    def __init__(self):
        print("Notifier: Екземпляр створено")

    def __del__(self):
        print("Notifier: Екземпляр знищено")


notifier1 = Notifier() # Виклик конструктора - створення
                       # екземляру класу Notifier
notifier2 = notifier1  # Створення посилання на екземпляр класу

del notifier1 # Виклик деструктора не буде здійснено, бо є
              # ще одне посилання (notifier2) на цей об’єкт
del notifier2 # Здійснюється виклик деструктора

print("Програму завершено")
