class Vector2D:
    def __init__(self, x, y):
        self.x = x  # Координата x вектора
        self.y = y  # Координата y вектора

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

if __name__ == "__main__":
    v1 = Vector2D(1, 3)
    v2 = Vector2D(4, 2)

    v3 = Vector2D(v1.x + v2.x, v1.y + v2.y)

