import time
import matplotlib.pyplot as plt

import lab_1.src.sorting.good_sorts as good_sorts
import lab_1.src.sorting.bad_sorts as bad_sorts 


def time_one(sort_func, L, time_factor=1000):
    start = time.perf_counter() * time_factor
    sort_func(L)
    end = time.perf_counter() * time_factor
    return end - start


def run():
    algorithms = [
        (good_sorts.mergesort, "Merge Sort (recursive)"),
        (good_sorts.bottom_up_mergesort, "Merge Sort (bottom-up iterative)"),
    ]

    rng = range(0, 5000, 50)  
    time_factor = 1000  # ms

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing", label, "...")
        for n in rng:
            L = bad_sorts.create_random_list(n, 100000)

            best_time = float("inf")
            for _ in range(5):
                L_copy = L.copy()
                t = time_one(sort_func, L_copy, time_factor)
                best_time = min(best_time, t)

            runtimes.append(best_time)

        plt.plot(rng, runtimes, label=label)

    plt.title("Experiment 7 - Merge Sort: recursive vs bottom-up iterative")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run()
