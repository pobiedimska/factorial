# цикл
def factorial_for(n):
    result = 1
    if n <= 1:
        return 1
    for i in range(n):
        result *= (i + 1)
    return result


# обычная рекурсия
def factorial_recursion(n, acc=1):
    if n <= 1:
        return acc
    return factorial_recursion(n - 1, acc * n)


# факториал с использованием логарифма
def ln_factorial(n, acc=0):
    if n <= 1:
        return acc
    return ln_factorial(n - 1, acc + math.log(n))


def factorial_log(f):
    return round(math.exp(ln_factorial(f)))


# начиная с этого момента и дальше мысли, которые я нашла по ссылке https://bioinfo.iric.ca/factorial-and-log-factorial/
# и которые были адаптированны и исправленны мной

# деление факториала по середине с использованием рекурсии
def create_range(bottom_edge, top_edge):
    if bottom_edge + 1 < top_edge:
        middle = (bottom_edge + top_edge) // 2
        return create_range(bottom_edge, middle) * create_range(middle + 1, top_edge)
    elif bottom_edge == top_edge:
        return bottom_edge
    return bottom_edge * top_edge


def factorial_split(n):
    if n <= 1:
        return 1
    return create_range(1, n)


# по формуле Стирлинга https://en.wikipedia.org/wiki/Stirling%27s_approximation
def factorial_stirling(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


# разложение в ряд Стирлинга через первые числа Бернулли
# (если честно, я еще не до конца поняла, как это работает, но мне кажется, что закоментированный кол правильнее)
def log_stirling(n):
    # sum = 0
    # числа Бернулли
    # b = [1, -0.5, 1 / 6, 0, -1 / 30, 0, 1 / 42, 0, -1 / 30,
    #     0, 5 / 66, 0, -691 / 2730, 0, 7 / 6, 0, -3617 / 510,
    #     0, 43867 / 798, 0, -174611 / 330]
    # for i in range(11):
    #    sum += b[2 * i] / (2 * i * (2 * i - 1) * n ** (2 * i - 1))
    # return sum
    fn = float(n)
    fn = n * math.log(fn) + math.log(2 * math.pi * fn) / 2 - fn + \
         (fn ** -1) / 12 - (fn ** -3) / 360 + (fn ** -5) / 1260 - \
         (fn ** -7) / 1680 + (fn ** -9) / 1188
    return fn

import sys

sys.setrecursionlimit(1000000)
import math


# зберігаємо значення певних факторіалів для пришвидчення роботи програми
def test_saved(saved, approx):
    value = list(range(0, 100, 5))
    if approx:
        if saved:
            value_saved = {1: 1}
            for num in value:
                log_fact_approx_saved(num, value_saved)
        else:
            for num in value:
                log_stirling(num)
    else:
        if saved:
            value_saved = {1: 1}
            for num in value:
                log_fact_exact_saved(num, value_saved)
        else:
            for num in value:
                log_fact_tree(num)


def factorial_math(n):
    return math.factorial(n)


for i in range(11):
    print("Recursion result of   " + str(i) + " is " + str(factorial_recursion(i)))
    print("For result of   " + str(i) + " is " + str(factorial_for(i)))
    print("Split result of " + str(i) + " is " + str(factorial_split(i)))
    print("Math result of  " + str(i) + " is " + str(factorial_math(i)))
    print("Logarithm result of  " + str(i) + " is " + str(factorial_log(i)))
    print("Stirling approximation result of  " + str(i) + " is " + str(factorial_stirling(i)))


import timeit

num = 100
rep = 20
print("\nLet\'s find out which way is the fastest:")
time_recursion = timeit.timeit("factorial_recursion(" + str(num) + ")", setup="from __main__ import factorial_recursion", number=rep)
time_for = timeit.timeit("factorial_for(" + str(num) + ")", setup="from __main__ import factorial_for", number=rep)
time_math = timeit.timeit("factorial_math(" + str(num) + ")", setup="from __main__ import factorial_math", number=rep)
time_split = timeit.timeit("factorial_split(" + str(num) + ")", setup="from __main__ import factorial_split", number=rep)
time_log = timeit.timeit("factorial_log(" + str(num) + ")", setup="from __main__ import factorial_log", number=rep)
time_stirling = timeit.timeit("factorial_stirling(" + str(num) + ")", setup="from __main__ import  factorial_stirling", number=rep)

print("factorial_recursion: " + str(time_recursion))
print("factorial_for:       " + str(time_for))
print("factorial_math:      " + str(time_math))
print("factorial_split:     " + str(time_split))
print("factorial_log:       " + str(time_log))
print("factorial_stirling:  " + str(time_stirling))