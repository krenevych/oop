from random import randint

COMP_RANGE = 1000

def generate(fname, vector_num, max_dim):
    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(vector_num):
            dim = randint(1, max_dim)
            for i in range(dim):
                v = randint(-COMP_RANGE, COMP_RANGE)
                print("%5d" % v, end=" ", file=f_out)
            print(file=f_out)
        print(file=f_out)


if __name__ == "__main__":
    generate("input01.txt", 10, 10)
    generate("input02.txt", 100, 50)
    generate("input03.txt", 500, 100)
    generate("input04.txt", 5000, 1000)
