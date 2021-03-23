from random import randint

N_MAXKEY = 99

operators = ["+", "-", "*"]

def generate(fname, lines, number):
    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(lines):
            number_in_line = randint(1, number)
            for j in range(number_in_line):
                coefCount = randint(1, 2)
                n = randint(1, N_MAXKEY)
                if coefCount == 1:
                    print("%d" % n, end="  ", file=f_out)
                else:
                    d = randint(2, N_MAXKEY)
                    print("%s" % ("%d/%d" % (n, d)), end="  ", file=f_out)
                operator_index = randint(0, 2)
                operator = operators[operator_index]
                print("%s" % operator, end="  ", file=f_out)

            n = randint(1, N_MAXKEY)
            print("%d" % n, file=f_out)

        print(file=f_out)


if __name__ == "__main__":
    generate("input01.txt", 15, 30)

