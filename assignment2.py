# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 2 - "Functions, Sets, and Sums"
# Kevin Zielinski

# Acknowledgements:
# I worked alone


from itertools import chain, combinations


def get_function_type(func, func_domain, func_co_domain):
    func_type = ""
    is_total = True
    is_injection = True
    func_range = set()
    for i in func_domain:
        image = func(i)
        if image is None or image not in func_co_domain:
            is_total = False
        elif image in func_range:
            is_injection = False
        else:
            func_range.add(func(i))
    is_surjection = func_co_domain == func_range
    is_bijection = is_injection and is_surjection
    return "Is total = " + str(is_total) + " Is injection = " + str(is_injection) + " Is surjection = " + str(is_surjection) + " Is bijection = " + str(is_bijection)


def square(i):
    return i ** 2


def identity(i):
    return i


def decrement(i):
    return i - 1


def increment(i):
    return i + 1


def half(i):
    return int(i / 2)


def sum_geometric_series_loop(a, r, n):
    s = 0
    for i in range(n + 1):
        s += a * r ** i
    return s


def sum_geometric_series_formula(a, r, n):
    return (a * r ** (n + 1) - 1) / (r - 1)


def sum_arithmetic_series_loop(a, d, n):
    s = 0
    for i in range(n + 1):
        s += a + (d * i)
    return s


def sum_arithmetic_series_formula(a, d, n):
    return (n + 1) * a + d * n * (n + 1) / 2


def compare_sums(name, loop, formula):
    print(name, loop, formula, loop == formula)


def sum_counting_loop(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s


def sum_counting_formula(n):
    return n*(n+1)/2


def sum_squares_loop(n):
    s = 0
    for i in range(n + 1):
        s += i**2
    return s


def sum_squares_formula(n):
    return n*(n + 1)*(2*n + 1)/6


def sum_cubes_loop(n):
    s = 0
    for i in range(n + 1):
        s += i ** 3
    return s


def sum_cubes_formula(n):
    return (n**2)*((n+1)**2)/4


def generate_binary_number(binary_numbers):
    new_b = "0."
    for i in range(2, len(binary_numbers[0])):
        digit = "1" if binary_numbers[i - 2][i] == "0" else "0"
        new_b += digit
    return new_b


# X ∪ Y
def set_union(set1, set2):
    return set1.union(set2)


# X ∩ Y
def set_intersection(set1, set2):
    return set1.intersection(set2)


# X − Y
def set_difference(set1, set2):
    return set1.difference(set2)


# X ∆  Y
def set_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


# X x Y
def set_cartesian_product(set1, set2):
    return str([(a, b) for a in set1 for b in set2]).replace("[", "{").replace("]", "}")


# P(X)
def set_power_set(set1):
    s = list(set1)
    return str(set(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))).replace("(", "{").replace(")", "}")


def q1():
    func_domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    func_codomain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print("Domain = ", func_domain)
    print("Codomain = ", func_codomain)
    print("Square function: ", get_function_type(square, func_domain, func_codomain))
    print("Identity function: ", get_function_type(identity, func_domain, func_codomain))
    print("Decrement function: ", get_function_type(decrement, func_domain, func_codomain))
    print("Increment function: ", get_function_type(increment, func_domain, func_codomain))
    print("Half function: ", get_function_type(half, func_domain, func_codomain))
    print()


def q2():
    x = {"a", "ab", "abc", "abcd"}
    y = {"a", "bb", "ccc", "dddd"}
    print("x = ", x)
    print("y = ", y)
    print("union: ", set_union(x, y))
    print("intersection: ", set_intersection(x, y))
    print("difference: ", set_difference(x, y))
    print("symmetric difference: ", set_symmetric_difference(x, y))
    print("cartesian product: ", set_cartesian_product(x, y))
    print("power set: ", set_power_set(x))
    print()


def q3():
    compare_sums("Geometric series", sum_geometric_series_loop(5, 6, 7), sum_geometric_series_formula(5, 6, 7))
    compare_sums("Arithmetic series", sum_arithmetic_series_loop(5, 6, 7), sum_arithmetic_series_formula(5, 6, 7))
    compare_sums("Sum of counting numbers", sum_counting_loop(10), sum_counting_formula(10))
    compare_sums("Sum of squares", sum_squares_loop(10), sum_squares_formula(10))
    compare_sums("Sum of squares", sum_squares_loop(10), sum_squares_formula(10))
    compare_sums("Sum of cubes", sum_cubes_loop(10), sum_cubes_formula(10))
    print()


def q4():
    list_b = ["0.010011", "0.101010", "0.111000", "0.000111", "0.111111", "0.111000"]
    new_b = generate_binary_number(list_b)
    print("Binary Numbers are: ", list_b)
    print("New Number is: ", new_b)
    print()


def main():
    q1()
    q2()
    q3()
    q4()


if __name__ == "__main__":
    main()
