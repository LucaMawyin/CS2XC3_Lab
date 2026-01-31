from sorting import bad_sorts as bs
from sorting import good_sorts as gs
import sys


import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(2000)

def run():
    algorithms = [
        (gs.quicksort, "Quick Sort"),
        (gs.mergesort, "Merge Sort"),
        (gs.heapsort, "Heap Sort")
    ]
    
    n = 1000
    swap_count = [i for i in range(0, 501, 5)]
    run_avg = 5

    time_factor = 1000 # seconds -> milliseconds

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing",label,"...")
        for swap in swap_count:
            total_time = 0
            for _ in range(run_avg):   

                L = bs.create_near_sorted_list(n, 100000, swap)
                
                start = time.perf_counter() * time_factor
                sort_func(L)
                end = time.perf_counter() * time_factor
                
                total_time += end - start

            runtimes.append(total_time/run_avg)
        
        plt.plot(swap_count, runtimes, label=label)
        

    plt.title(f"Sorting Algorithm Performance of Near Sorted Lists of Length {n}")
    #plt.yscale('log')
    plt.xlabel("Number of Swaps")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    run()
