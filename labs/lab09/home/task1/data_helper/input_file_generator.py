# -*- coding: utf8 -*-

from random import randint

N_MAXKEY = 25
MULT = 4

ACTIONS = [
    "teach humanitarian",  # вивчити гуманітарну дисципліну
    "teach natural",  # вивчити природничу дисципліну
    "obtain scholarship",  # отримати стипендію
    "obtain help",  # отримати допомогу від батьків
    "pay hostel",  # заплатити за гуртожиток
    "pay canteen",  # заплатити за харчування у столовій
]

DIRECTIONS = [
    "humanitarian",  # гуманітарни напрям
    "natural",  # природничий напрям
    "natural-humanitarian",  # природничо-гуманітарний напрям
]

def generate(fname, actions_number):
    ACTIONS_COUNT = len(ACTIONS)
    DIRECTIONS_COUNT = len(DIRECTIONS)

    with open(fname, "w", encoding='utf-8') as f_out:
        direction = DIRECTIONS[randint(0, DIRECTIONS_COUNT - 1)]
        print("%30s" % direction, file=f_out)
        credit_count = randint(200, 600)
        print("%30s" % credit_count, file=f_out)
        start_money = randint(2000, 60000)
        print("%30s" % start_money, file=f_out)

        for i in range(actions_number):

            action = ACTIONS[randint(0, ACTIONS_COUNT - 1)]
            print("%30s" % action, file=f_out, end=" ")
            if action == "teach humanitarian":
                action_prop = randint(1, 10)
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "teach natural":
                action_prop = randint(1, 10)
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "obtain scholarship":
                action_prop = 1500
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "obtain help":
                action_prop = randint(1, 10) * 100
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "pay hostel":
                action_prop = 300
                print("%5s" % action_prop, file=f_out, end=" ")
            elif action == "pay canteen":
                action_prop = randint(50, 100)
                print("%5s" % action_prop, file=f_out, end=" ")

            print(file=f_out)



if __name__ == "__main__":
    for i in range(1, 15):
        d = "" if i >= 10 else "0"
        f_name = "input" + d + str(i) + ".txt"
        generate(f_name, 1000)
