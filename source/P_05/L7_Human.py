# Базовий клас Істота
class Human:

    def __init__(self):
        """ Конструктор """
        self._health = 100  # Рівень здоров'я у відсотках

    def eat(self, food):
        if food == "junk food":         # шкідливий продукт
            self._health -= 20          # погіршує здоров'я
        elif food == "healthy food":    # корисний продукт
            self._health += 20          # покращує здоров'я

        self._health = self._health if self._health > 0 else 0
        self._health = self._health if self._health < 100 else 100

