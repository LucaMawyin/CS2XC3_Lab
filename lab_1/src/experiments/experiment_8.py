import time
import matplotlib.pyplot as plt

import lab_1.src.sorting.bad_sorts as bad_sorts
import lab_1.src.sorting.good_sorts as good_sorts


def time_one(sort_func, L, time_factor=1000):
    start = time.perf_counter() * time_factor
    sort_func(L)
    end = time.perf_counter() * time_factor
    return end - start


def run():
    algorithms = [
        (bad_sorts.insertion_sort2, "Insertion Sort (optimized)"),
        (good_sorts.mergesort, "Merge Sort"),
        (good_sorts.quicksort, "Quick Sort"),
    ]

    rng = range(0, 301, 5)   # small list lengths
    time_factor = 1000       # ms

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing", label, "...")
        for n in rng:
            if n == 0: # avoid crash at n = 0
                runtimes.append(0)
                continue

            swaps = max(1, n // 20)   # ~5% swaps so we have near sorted
            L = bad_sorts.create_near_sorted_list(n, 100000, swaps)
            # L = bad_sorts.create_random_list(n, 100000)
            # since insertion sort performed at best when the list is near sorted
            # that why I decided to not create random list here

            best_time = float("inf")
            for _ in range(5):
                L_copy = L.copy()
                t = time_one(sort_func, L_copy, time_factor)
                best_time = min(best_time, t)

            runtimes.append(best_time)

        plt.plot(rng, runtimes, label=label)

    plt.title("Experiment 8 - Small lists: Insertion vs Merge vs Quick")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run()
