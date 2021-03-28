from random import randint

MAX_COEF = 999


def generate(fname, max_pow, coef_number):
    assert max_pow > coef_number
    polymon = {}
    for i in range(coef_number):
        while True:
            power = randint(0, max_pow)
            if power not in polymon:
                break

        polymon[power] = randint(-MAX_COEF, MAX_COEF)

    with open(fname, "w", encoding='utf-8') as f_out:
        for power, coef in polymon.items():
            print("%4d %4d" % (power, coef), file=f_out)

        print(file=f_out)


if __name__ == "__main__":
    generate("input01.txt", 40, 30)
    generate("input02.txt", 40, 30)
