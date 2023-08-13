# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 7 - "Discrete Probability"
# Kevin Zielinski

# Acknowledgements:
# worked with the class

from math import perm, comb
import matplotlib.pyplot as plt
import numpy as np
import texttable as tt


# C(n-1, k-1) hk (1-h)n-k
def prob(n, k, h):
    return 0 if n < k else comb(n - 1, k - 1) * (h ** k) * ((1 - h) ** (n - k))


# cumulative probability
def cprob(n, k, h):
    return sum([prob(i, k, h) for i in range(n + 1)])


# expected value
def ev(k, h):
    max_n = 100
    return sum([n * prob(n, k, h) for n in range(1 + max_n)])


# see: https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
def plot_distribution(title, file_name, list_k, df, h):
    max_n = 21
    # x-axis = n
    x_axis = [n for n in range(max_n)]
    x = np.arange(len(x_axis))  # the label locations
    # y-axis = probability p(X=n)
    width = 0.25  # the width of the bars
    num = len(list_k)
    for i in range(num):
        k = list_k[i]
        y = [df(n, k, h) for n in range(max_n)]
        fig, ax = plt.subplots()
        ax.bar(x - width * i / num, y, width, label="k=" + str(k), color=['black', 'red', 'green', 'blue', 'cyan'])

    ax.set_xlabel('Number of Tosses (n)')
    ax.set_ylabel('Probability of k heads on toss n')
    ax.set_title(title)
    ax.set_xticks(x, x_axis)
    ax.legend()
    fig.tight_layout()
    plt.savefig(file_name)
    plt.show()


def make_ev_table():
    data = [["p(H)", "k (num heads)", "Expected Value"]]
    for h in [.25, .50, .75, 1]:
        for k in [5, 10, 15, 20]:
            data.append([h, k, round(ev(k, h), 2)])
    t = tt.Texttable()
    t.set_cols_align(["r", "r", "r"])
    t.set_cols_dtype(["f", "i", "f"])
    t.set_cols_valign(["t", "t", "t"])
    t.add_rows(data)
    print(t.draw())


def main():
    assn = "assignment7"
    list_k = [5, 10]
    for h in [.25, .50, .75, 1]:
        title = "Coin Toss with p(H)=" + str(h)
        plot_distribution("PDF for " + title, assn + "-pdf-" + str(h) + ".png", list_k, prob, h)
        plot_distribution("CDF for " + title, assn + "-cdf-" + str(h) + ".png", list_k, cprob, h)
    make_ev_table()


if __name__ == "__main__":
    main()
