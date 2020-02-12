class Logged:
    def log(self):
        print("========= Клас:", self.__class__.__name__)
        print("Кличка тварини:", self._name)
        print("Кількість лап: ", self._legs)
        print("Кількість бліх:", self._fleas)
