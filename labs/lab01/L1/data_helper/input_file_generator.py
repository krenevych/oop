from random import randint

N_MAXKEY = 100

def generate(fname, equations_number):
    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(equations_number):
            coef2 = randint(-N_MAXKEY, N_MAXKEY)
            coef1 = randint(-N_MAXKEY, N_MAXKEY)
            coef0 = randint(-N_MAXKEY, N_MAXKEY)
            print("%4d %4d %4d" % (coef2, coef1, coef0), file=f_out)

        print(file=f_out)


if __name__ == "__main__":
    generate("input01.txt", 100)
    generate("input02.txt", 500)
    generate("input04.txt", 1000)
