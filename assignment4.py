# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 4 - "Empirical Performance of Search Algorithms"
# Kevin Zielinski

# Acknowledgements:
# I worked with the class

import pandas as pd
import matplotlib.pyplot as plt
import random
import time


def plot_times(dict_searches, sizes, trials, searches, file_name):
    search_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for search in searches:
        search_num += 1
        d = dict_searches[search.__name__]
        x_axis = [j + 0.05 * search_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=search.__name__)
    plt.legend()
    plt.title("Runtime of search algorithms")
    plt.xlabel("Number of elements")
    plt.ylabel("Time for " + str(trials) + " 100 trials (ms)")
    plt.savefig(file_name)
    plt.show()


def run_searches(searches, sizes, trials):
    dict_searches = {}
    for search in searches:
        dict_searches[search.__name__] = {}
    for size in sizes:
        for search in searches:
            dict_searches[search.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = random_list(size)
            idx = random.randint(0, size - 1)
            key = arr[idx]
            for search in searches:
                start_time = time.time()
                if search.__name__ == 'randomized_binary_search':
                    idx_found = search(arr, 0, size - 1, key)
                else:
                    idx_found = search(arr, key)
                end_time = time.time()
                if idx_found != idx:
                    print(search.__name__, "wrong index found", idx, idx_found, arr)
                net_time = end_time - start_time
                dict_searches[search.__name__][size] += 1000 * net_time
    return dict_searches


def print_times(dict_searches):
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_searches).T
    print(df)


def random_list(size):
    l = [0] * size
    for i in range(1, size):
        r = random.randint(1, 10)
        l[i] = l[i - 1] + r
    return l


def native_search(arr, key):
    return arr.index(key)


def linear_search(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


def binary_search_iterative(arr, key):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = int((l + r) / 2)
        if arr[m] == key:
            return m
        elif arr[m] < key:
            l = m + 1
        else:
            r = m - 1
    if arr[l] == key:
        return l
    else:
        return -1


def binary_search_recursive_helper(arr, l, r, key):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive_helper(arr, l, mid - 1, key)
        else:
            return binary_search_recursive_helper(arr, mid + 1, r, key)
    else:
        return -1


def binary_search_recursive(arr, key):
    return binary_search_recursive_helper(arr, 0, len(arr) - 1, key)


def getRandom(x, y):
    tmp = (x + random.randint(0, 100000) % (y - x + 1))
    return tmp


def randomized_binary_search(arr, l, r, key):
    if r >= l:
        mid = getRandom(l, r)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return randomized_binary_search(arr, l, mid - 1, key)
        return randomized_binary_search(arr, mid + 1, r, key)
    return -1


def main():
    sizes = [10, 100, 1000, 10000]
    searches = [native_search, linear_search, binary_search_iterative, binary_search_recursive,
                randomized_binary_search]
    trials = 100
    dict_searches = run_searches(searches, sizes, trials)
    print_times(dict_searches)
    plot_times(dict_searches, sizes, trials, searches, "assignment4.png")


if __name__ == "__main__":
    main()

