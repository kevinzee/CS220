# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 9 - "Linear Homogeneous Recurrences"
# Kevin Zielinski
import math

import numpy as np


# Acknowledgements:
# I worked alone
def solve_recurrence(desc, formula):
    print(desc)
    print("The Provided Formula is:", formula)
    c1, c0, a0, a1 = extract_parameters(formula)
    recurrence = "a(n) = " + str(c1) + "*a(n-1) + " + str(c0) + "*a(n-2)"
    print("The Reconstructed Formula is:", recurrence)
    r1, r2 = solve_characteristic_equations(c0, c1)
    distinct = r1 != r2
    x0, x1 = get_coefficients(a0, a1, r1, r2)
    r1, r2, x0, x1 = round_numbers(r1, r2, x0, x1)
    formula = f"a(n) = {x0} x {r1}^n " + (f"{x1} {r2}^n" if distinct else f"{x1} n {r2}^n")
    print("The closed-form formulas is", formula)
    a2_recurrence = c1 * a1 + c0 * a0
    a2_formula = x0 * r1 ** 2 + x1 * (2 if not distinct else 1) * r2 ** 2
    print("a(2) using recurrence", a2_recurrence)
    print("a(2) formula", a2_formula)
    print()


def round_numbers(r1, r2, x0, x1):
    x0 = f2i(x0)
    x1 = f2i(x1)
    r1 = f2i(r1)
    r2 = f2i(r2)
    return r1, r2, x0, x1


def f2i(f):
    return int(round(f)) if round(f, 5) == round(f) else f


def get_coefficients(a0, a1, r1, r2):
    distinct = r1 != r2
    A = np.array([[r1 ** 0, (0 if not distinct else 1) * r2 ** 0], [r1 ** 1, (1 if not distinct else 1) * r2 ** 1]])
    B = np.array([a0, a1])
    X = np.linalg.solve(A, B)
    print("The coefficients are", X[0], X[1])
    return X[0], X[1]


def solve_characteristic_equations(c0, c1):
    characteristic_equation = "r^2 - " + ("" if c1 == 1 else str(c1)) + "r - " + str(c0)
    print("characteristic equation is", characteristic_equation)
    a = 1
    b = -1 * c1
    c = -1 * c0
    junk = b ** 2 - 4 * a * c
    temp = math.sqrt(junk)
    r1 = ((-1 * b) + temp) / (2 * a)
    r2 = ((-1 * b) - temp) / (2 * a)
    print("The roots are ", r1, r2)
    return r1, r2


def extract_parameters(formula):
    parts = formula.split(",")
    x0 = my_float(get_rhs(parts[0]))
    x1 = my_float(get_rhs(parts[1]))
    rhs = get_rhs(parts[2])
    letter = parts[2].strip()[0]
    terms = rhs.split("+")
    c1 = get_coef(terms[0], letter)
    c0 = get_coef(terms[1], letter)
    return c1, c0, x0, x1


def get_rhs(equation):
    parts = equation.split("=")
    return parts[1].strip()


def my_float(s):
    f = s.strip()
    return 1.0 if f == "" else float(f)


def get_coef(term, letter):
    parts = term.split(letter)
    return my_float(parts[0])


def main():
    assn = "assignment9"
    solve_recurrence("fibonacci", "f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2)")
    solve_recurrence("slide 22", "a(0) = 2, a(1) = 7, a(n) = a(n-1) + 2a(n-2)")
    solve_recurrence("slide 26", "a(0) = 1, a(1) = 6, a(n) = 6a(n-1) + -9a(n-2)")
    solve_recurrence("example from google doc", "r(0) = 2, r(1) = 3, r(n) = 5r(n-1) + -6r(n-2)")
    solve_recurrence("example from web", "r(0) = 2, r(1) = 5, r(n) = 6r(n-1) + -9r(n-2)")
    solve_recurrence("example from web", "r(0) = 1, r(1) = 2, r(n) = 1r(n-1) + 2r(n-2)")
    solve_recurrence("example from exam", "r(0) = 0, r(1) = 1, r(n) = 1r(n-1) + 2r(n-2)")
    solve_recurrence("example from prof", "r(0) = 1, r(1) = 2, r(n) = 12r(n-1) + -27r(n-2)")


if __name__ == "__main__":
    main()
