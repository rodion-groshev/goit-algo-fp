import numpy as np


def generate_numbers(step):
    first = np.random.randint(1, 7, step)
    second = np.random.randint(1, 7, step)
    sum_lst = list(map(lambda x, y: x + y, first, second))
    return sum_lst


def monte_carlo(step):
    res = {}
    numbers = generate_numbers(step)
    for num in range(2, 13):
        inside = sum(num == x for x in numbers)
        ratio = inside / step
        res[num] = round(ratio * 100, 2)
    return res


# Отримані результати майже ідентичні з наведеними у завданні
print(monte_carlo(50000))
