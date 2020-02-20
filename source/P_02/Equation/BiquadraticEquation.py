from source.P_02.Equation.QuadraticEquation import QuadraticEquation


class BiquadraticEquation (QuadraticEquation):
    """  Клас біквадратне рівняння виду ax**4 + bx**2 + c = 0 """

    def solve(self):
        result = []
        solutions = super().solve()  # розв'язки квадратного рівняння при заміні y = x**2
        for y in solutions:
            if y == "inf":
                result.append("inf")
            elif y == 0:
                result.append(0)
            elif y > 0:
                x1 = y ** 0.5
                x2 = -x1
                result.append(x1)
                result.append(x2)

        return result


if __name__ == "__main__":

    equation_list = []  # список рівнянь
    equation_list.append(BiquadraticEquation(0, 4, 1))   # розв'язків немає
    equation_list.append(BiquadraticEquation(0, 0, 0))   # розв'язками є вся числова вісь
    equation_list.append(BiquadraticEquation(0, 0, 1))   # розв'язків немає
    equation_list.append(BiquadraticEquation(1, -3, 2))  # чотири розв'язки [1.0, -1.0, 1.4142135623730951, -1.4142135623730951]
    equation_list.append(BiquadraticEquation(1, -2, 1))  # два розв'язоки [1.0, -1.0]
    equation_list.append(BiquadraticEquation(1, 2, 4))   # розв'язків немає
    equation_list.append(BiquadraticEquation(1, 2, -3))  # два розв'язки [1.0, -1.0]

    for eq in equation_list:
        print(eq.solve())


