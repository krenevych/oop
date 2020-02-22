
print(eval('sqrt(25)')) # Буде породжена помилка,
# # оскільки eval не знає нічого про глобальну функцію sqrt
#
import math
print(eval('sqrt(25)', {"sqrt": math.sqrt}, {}))
