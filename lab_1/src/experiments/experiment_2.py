import time
import matplotlib.pyplot as plt

import lab_1.src.sorting.bad_sorts as bad_sorts


def time_one(sort_func, L, time_factor=1000):
    start = time.perf_counter() * time_factor
    sort_func(L)
    end = time.perf_counter() * time_factor
    return end - start


def bubble_compare():
    algorithms = [
        (bad_sorts.bubble_sort, "Bubble (original)"),
        (bad_sorts.bubblesort2, "Bubble (variation)"),
    ]

    rng = range(0, 1000, 10)
    time_factor = 1000

    plt.figure(figsize=(10, 6))
    for sort_func, label in algorithms:
        runtimes = []
        print("testing", label, "...")
        for n in rng:
            L = bad_sorts.create_random_list(n, 100000)
            runtimes.append(time_one(sort_func, L, time_factor))
        plt.plot(rng, runtimes, label=label)

    plt.title("Experiment 2 - Bubble sort: original vs variation")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


def selection_compare():
    algorithms = [
        (bad_sorts.selection_sort, "Selection (original)"),
        (bad_sorts.selection_sort2, "Selection (min+max variation)"),
    ]

    rng = range(0, 1000, 10)
    time_factor = 1000

    plt.figure(figsize=(10, 6))
    for sort_func, label in algorithms:
        runtimes = []
        print("testing", label, "...")
        for n in rng:
            L = bad_sorts.create_random_list(n, 100000)
            runtimes.append(time_one(sort_func, L, time_factor))
        plt.plot(rng, runtimes, label=label)

    plt.title("Experiment 2 - Selection sort: original vs min+max variation")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


def run():
    bubble_compare()
    selection_compare()


if __name__ == "__main__":
    run()
