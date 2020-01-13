from time import clock  # підключення функції clock


def benchmark(f):
    def _benchmark(*args, **kw):
        # вимірюємо час перед викликом функції
        current_time = clock()
        rez = f(*args, **kw)  # викликаємо f
        # обчилюємо різницю у часі
        dt = clock() - current_time
        print('Час виконання функції %1.5f cек' % dt)
        return rez

    return _benchmark
