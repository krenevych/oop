from random import randint

N_MAXKEY = 25
MULT = 4


def generate(fname, lines, number):
    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(lines):
            number_in_line = randint(1, number)
            for j in range(number_in_line):
                coefCount = randint(1, 2)
                n = randint(-N_MAXKEY, N_MAXKEY)
                if coefCount == 1:
                    print("%d" % (n), end="  ", file=f_out)
                else:
                    d = randint(2, N_MAXKEY)
                    print("%d/%d" % (n, d), end="  ", file=f_out)

            print(file=f_out)
        print(file=f_out)


if __name__ == "__main__":
    generate("input01.txt", 1, 30)
    generate("input02.txt", 10, 50)
    generate("input03.txt", 1000, 50)
