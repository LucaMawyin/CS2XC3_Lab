from sorting import bad_sorts as bs
from sorting import good_sorts as gs

import time
import matplotlib.pyplot as plt


def run():
    algorithms = [
        (gs.quicksort_copy, "Quick Sort"),
        (gs.mergesort, "Merge Sort"),
        (gs.heapsort, "Heap Sort")
    ]
    
    rng = range(0, 1000,10) 
    time_factor = 1000 # seconds -> milliseconds

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing",label,"...")
        for i in rng:
            L = bs.create_random_list(i, 100000)
            
            start = time.perf_counter() * time_factor
            sort_func(L)
            end = time.perf_counter() * time_factor
            
            runtimes.append(end - start)
        
        plt.plot(rng, runtimes, label=label)
        

    plt.title("Sorting Algorithm Performance Comparison")
    #plt.yscale('log')
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    



if __name__ == '__main__':
    run()
