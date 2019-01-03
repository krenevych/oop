class Notifier:
    def __init__(self, name):
        self.name = name  # створюється поле self.name
        print("Notifier: Екземпляр %s створено" % self.name)

    def __del__(self):
        print("Notifier: Екземпляр %s знищено" % self.name)


notifier1 = Notifier("Notifier1")
