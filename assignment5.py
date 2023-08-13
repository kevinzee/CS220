# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 5 - "Evaluating and Ranking of Functions"
# Kevin Zielinski

# Acknowledgements:
# I worked alone
import inspect
import math
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from itertools import product
from math import log, factorial, log10


def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after the word return
    return body[7 + idx:].strip()


def f0(n):
    return n


def f1(n):
    return 1.5**n


def f2(n):
    return 8*n**3 + 17*n**2 + 111


def f3(n):
    return log(n)**2


def f4(n):
    return 2**n


def f5(n):
    return log(log(n))


def f6(n):
    return n**2 * log(n)**3


def f7(n):
    return 2**n + (n**2 + 1)


def f8(n):
    return n**3 + n * log(n)**2


def f9(n):
    return 10000


def f10(n):
    return factorial(n)


def plot_functions(dict_functions, sizes, functions, file_name):
    func_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for func in functions:
        func_num += 1
        d = dict_functions[func.__name__]
        x_axis = [j + 0.05 * func_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        our_label = func.__name__ + "= " + func_body(func)
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=our_label)
    plt.legend()
    plt.title("Relative value of Functions")
    plt.xlabel("n")
    plt.ylabel("log 10(f(n))")
    plt.savefig(file_name)
    plt.show()


def calc_functions(functions, sizes):
    dict_functions = {}
    for func in functions:
        dict_functions[func.__name__] = {}
    for size in sizes:
        for func in functions:
            dict_functions[func.__name__][size] = log10(func(size))
    return dict_functions


def print_functions(dict_functions):
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_functions).T
    print(df)
    print()


def rank_functions(dict_functions, size):
    values = {}
    for func in dict_functions:
        values[func] = dict_functions[func][size]
    dict_sorted = dict(sorted(values.items(), key=lambda item: item[1]))
    print("Ranking of log of functions for n = ", size)
    for func in dict_sorted:
        print(func, dict_sorted[func])


def main():
    assn = "assignment5"
    sizes = [10*i for i in range(1, 11)]
    functions = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    dict_functions = calc_functions(functions, sizes)
    print_functions(dict_functions)
    plot_functions(dict_functions, sizes, functions, assn + ".png")
    rank_functions(dict_functions, sizes[0])
    print()
    rank_functions(dict_functions, sizes[-1])


if __name__ == "__main__":
    main()
