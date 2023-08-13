# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 8 - "Divide-and-Conquer Recurrences"
# Kevin Zielinski

# Acknowledgements:
# I worked alone
import inspect
import texttable as tt


def master_theorem(a, b, c):
    lhs = a
    rhs = b ** c
    result = f"Solution with a = {a} b = {b} c = {c} is f(n) = Θ("
    if lhs < rhs:
        result += f"n^{c}"
    elif lhs == rhs:
        result += f"n^{c} log(n)"
    else:
        result += f"n^(log_{b} {a})"
    result += ")"
    return result


def use_master_theorem(function, description, a, b, c):
    print(description)
    print(function)
    print(master_theorem(a, b, c))
    print()


def func_body(f):
    body = inspect.getsource(f)
    idx = body.index("return")
    return body[7 + idx:].strip()


# Merge Sort
def f1(f, n):
    return 0 if n == 1 else 2 * ff(f, n / 2) + n


# Binary Search
def f2(f, n):
    return 1 if n == 1 else 1 * ff(f, n / 2) + 1


# Fibonacci
def f3(f, n):
    return 0 if n == 0 else (1 if n == 1 else ff(f, n - 1) + ff(f, n - 2))


# Long Integer Multiplication
def f4(f, n):
    return 0 if n == 1 else 4 * ff(f, n / 2) + n


# Fast Long Integer Multiplication
def f5(f, n):
    return 0 if n == 1 else 3 * ff(f, n / 2) + n


# Matrix Multiplication
def f6(f, n):
    return 0 if n == 1 else 8 * ff(f, n / 2) + n ** 2


# Fast Matrix Multiplication
def f7(f, n):
    return 0 if n == 1 else 7 * ff(f, n / 2) + n ** 2


# Bubble Sort
def f8(f, n):
    return 0 if n == 1 else ff(f, n - 1) + n - 1


# Linear Search
def f9(f, n):
    return 1 if n == 1 else ff(f, n - 1) + 1


# Stooge Sort
def f10(f, n):
    return 0 if n == 1 else 3 * ff(f, int(2 * n / 3)) + 1


def call_and_print(func, n, desc, formula):
    data.append([func.__name__, desc, formula, func_body(func), n,
                 ff(func, n)])  # "No. ", "Description", "Formula", "Function", 'n', "F(n)"


dict_funcs = {}
data = [["No. ", "Description", "Formula", "Function Code", 'n', "F(n)"]]


def ff(f, n):
    func_name = f.__name__
    if func_name not in dict_funcs:
        dict_funcs[func_name] = {}
    dict_func = dict_funcs[func_name]
    if n not in dict_func:
        dict_func[n] = f(f, n)
    return dict_func[n]


def print_functions():
    for func in dict_funcs:
        print(func, dict_funcs[func])


def make_table(data):
    t = tt.Texttable(max_width=200)
    t.set_cols_align(["l", "l", "l", "l", "r", "r"])
    t.add_rows(data)
    print(t.draw())


def main():
    assn = "Assignment8"
    use_master_theorem("f(n) = f(n/2) + 2", "Binary Search:", 1, 2, 0)
    use_master_theorem("f(n) = 4f(n/2) + O(n)", "Big Integer Multiplication:", 4, 2, 1)
    use_master_theorem("f(n) = 3f(n/2) + O(n)", "Fast Addition of Integers:", 3, 2, 1)
    use_master_theorem("f(n) = 2f(n/2) + O(n)", "Merge Sort:", 2, 2, 1)
    use_master_theorem("f(n) = 8f(n/2) + O(n^2)", "Matrix Multiplication:", 8, 2, 2)
    use_master_theorem("f(n) = 7f(n/2) + O(n^2)", "Fast Matrix Multiplication:", 7, 2, 2)
    for n in [64, 256]:
        call_and_print(f9, n, "Linear Search", "f(n) = f(n-1) + 1")
        call_and_print(f2, n, "Binary Search", "f(n) = f(n/2) + 1")
        call_and_print(f8, n, "Bubble Sort", "f(n) = f(n-1) + n-1")
        call_and_print(f1, n, "Merge Sort", "f(n) = 2*f(n/2) + n")
        call_and_print(f10, n, "Stooge Sort", "f(n) = 3f(2n/3)")
        call_and_print(f4, n, "Long Integer Multiplication", "f(n) = 4f(n/2) + O(n)")
        call_and_print(f5, n, "Fast Long Integer Multiplication", "f(n) = 3f(n/2) + O(n)")
        call_and_print(f6, n, "Matrix Multiplication", "f(n) = 8f(n/2) + O(n^2)")
        call_and_print(f7, n, "Fast Matrix Multiplication", "f(n) = 7f(n/2) + O(n^2)")
        call_and_print(f3, n, "Fibonacci", "f(n) = f(n-1) + f(n-2)")
    make_table(data)


if __name__ == "__main__":
    main()




