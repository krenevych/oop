class Notifier:
    def __init__(self):
        print("Notifier: Екземпляр створено")
    def __del__(self):
        print("Notifier: Екземпляр знищено")

notifier = Notifier()   # список аргументів порожній
