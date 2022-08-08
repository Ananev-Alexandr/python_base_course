import itertools
import math


def primes():
    now_num = 2
    while True:
        if (math.factorial(now_num-1)+1) % now_num == 0:    # Теорема Вильсона
            yield now_num
        now_num += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
