# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 3 - "Induction and Recursion"
# Kevin Zielinski

# Acknowledgements:
# I worked alone
import math
import random


sqrt5 = math.sqrt(5)


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_formula(n):
    return (1 / sqrt5) * (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n)


def sum_fib_formula(n):
    s1 = sum_geometric_series_formula(1/sqrt5, (1 + sqrt5) / 2, n)
    s2 = sum_geometric_series_formula(1/sqrt5, (1 - sqrt5) / 2, n)
    s1 = round(s1, 0)
    s2 = round(s2, 0)
    return s1 + s2


def sum_fib_loop(n):
    return sum([fib_formula(i) for i in range(n + 1)])


def sum_geometric_series_formula(a, r, n):
    return (a * r ** (n + 1) - 1) / (r - 1)


def gcd_recursive(a, b):
    if a > b:
        return gcd_recursive(b, a)
    elif a == 0:
        return b
    else:
        return gcd_recursive(b % a, a)


# stamps[0] = 4 stamps stamps[1] = 5 stamps
def find_postage(amount, stamps):
    if amount == 12:
        stamps[0] += 3
        stamps[1] += 0
    elif amount == 13:
        stamps[0] += 2
        stamps[1] += 1
    elif amount == 14:
        stamps[0] += 1
        stamps[1] += 2
    elif amount == 15:
        stamps[0] += 0
        stamps[1] += 3
    else:
        stamps[0] += 1
        stamps[1] += 0
        find_postage(amount - 4, stamps)


def all_strings(alphabet, size):
    language = [""]
    for i in range(size):
        for c in alphabet:
            language += [word + c for word in language]
    return sorted(set(language), key=len)


def compare_results(name, result1, result2):
    result1 = round(result1, 4)
    result2 = round(result2, 4)
    print(name, result1, result2, result1 == result2)


def q1():
    for i in range(10):
        amount = random.randint(12, 100)
        stamps = [0, 0]
        find_postage(amount, stamps)
        print("Postage for amount:", amount, "is", stamps)
    print()


def q2():
    numbers = 10
    for n in range(2, numbers + 1):
        fr = fib_recursive(n)
        ff = fib_formula(n)
        compare_results("Fibonacci", fr, ff)
    print()


def q3():
    numbers = 10
    for n in range(2, numbers + 1):
        sfl = sum_fib_loop(n)
        sff = sum_fib_formula(n)
        compare_results("Fibonacci", sfl, sff)
    print()


def q4():
    for i in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        compare_results("GCD of " + str(a) + " and " + str(b), gcd_recursive(a, b), math.gcd(a, b))
    print()


def q5():
    print(all_strings(['a'], 10))
    print(all_strings(['a', 'b', 'c'], 3))
    print()


def main():
    q1()
    q2()
    q3()
    q4()
    q5()


if __name__ == "__main__":
    main()
