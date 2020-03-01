from source.P_06.L8_delattr import A


class B(A):
    pass

delattr(B, "method")  # Спроба видалення атрибуту method у класу B
