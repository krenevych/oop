# -*- coding: utf8 -*-

from random import randint

Speciality = {
    "Математика": 180,  # Математика, кількість студентів на курсі
    "Статистика": 150,  # Статистика
    "Середня освіта": 50,  # Середня освіта-математика
}

Exam = "Екзамен"
Credit = "Залік"

Discipline = [  # Дисципліна, іспит чи залік)
    {
        #  1 курс
        "Іноземна мова-1": Exam,
        "Математичний аналіз: функції однієї змінної": Exam,  #
        "Лінійна алгебра": Exam,  #
        "Аналітична геометрія": Exam,  #
        "Дискретна математика": Exam,  #

        "Фізична культура": Credit,  #
        "Об'єктно-орієнтовне програмування": Credit,  #
    },

    # 2 курс
    {
        "Диференціальні рівняння": Exam,  #
        "Математичний аналіз: функції багатьох змінних": Exam,  #
        "Дискретні ймовірносні простори": Exam,  #
        "Прикладне програмування": Exam,  #

        "Українська та зарубіжна культура": Credit,  #
        "Алгебра і теорія чисел": Credit,  #
    },

    # 3 курс
    {
        "Теорія ймовірностей": Exam,  #
        "Комплексний аналіз": Exam,  #
        "Функціональний аналіз": Exam,  #
        "Математична статистика": Exam,  #

        "Рівняння математичної фізики": Credit,  #
        "Теорія пружності": Credit,  #
        "Науковий образ світу": Credit,  #
    }
]

FigureNames = list(Speciality.keys())


def generate(fname):
    students = []
    with open("stud.txt", encoding='utf-8') as f_stud:
        for line in f_stud:
            students.append(line.strip())

    stud_distribution = {}
    for year in range(1, 4):
        for spec, student_spec_count in Speciality.items():
            stud_distribution[(year, spec)] = []
            for i in range(student_spec_count):
                students_num = len(students)
                stud_rand_num = randint(0, students_num - 1)
                student = students[stud_rand_num]
                stud_distribution[(year, spec)].append(student)
                students.remove(student)
            stud_distribution[(year, spec)].sort()

    with open(fname, "w", encoding='utf-8') as f_out:
        for spec in Speciality:
            for year in range(len(Discipline)):
                disc_year = Discipline[year]
                for disc in disc_year:
                    print("Speciality: %s" % spec, file=f_out)
                    print("Year of education: %s" % (year + 1), file=f_out)
                    print("Discipline: %s" % disc, file=f_out)
                    print("Type of control: %s" % Discipline[year][disc], file=f_out)
                    for stud in stud_distribution[(year + 1, spec)]:
                        mark = randint(47, 100)
                        print("%50s: %6d" % (stud, mark), file=f_out)


if __name__ == "__main__":
    generate("input02.txt")
