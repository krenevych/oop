from source.P_02.L2_Pets import Cat
from source.P_02.L3_Pet import Pet

if __name__ == "__main__":
    base = Pet("No name")  # екземпляр базового класу
    my_cat = Cat("Kuzya")  # кіт Кузя

    base.voice()
    my_cat.voice()
