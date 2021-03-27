# -*- coding: utf8 -*-

from random import randint

N_MAXKEY = 25
MULT = 4

Figures = {"Triangle" : 3,                     # Трикутник
           "Rectangle" : 2,                    # Прямокутник
           "Trapeze" : 4,                      # Трапеція
           "Parallelogram" : 3,                # Паралелограм
           "Circle" : 1,                       # Круг
           # "Ball" : 1,                         # Куля
           # "TriangularPyramid" : 2,            # Трикутна піраміда
           # "QuadrangularPyramid" : 3,          # Чотирикутна піраміда
           # "RectangularParallelepiped" : 3,    # Прямокутний паралелепіпед
           # "Cone" : 2,                         # Конус
           # "TriangularPrism": 4,               # Трикутна Призма
           }

FigureNames = list(Figures.keys())

def generate(fname, figures_number):
    FUGUGE_COUNT = len(FigureNames)

    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(figures_number):

            figure = FigureNames[randint(0, FUGUGE_COUNT - 1)]
            print("%30s" % figure, file=f_out, end=" ")

            val_num = Figures[figure]
            for i in range(val_num):
                val = randint(0, N_MAXKEY)
                print("%4d" % val, file=f_out, end=" ")

            print(file=f_out)



if __name__ == "__main__":
    generate("input01.txt", 100)
    generate("input02.txt", 500)
    generate("input03.txt", 1000)
