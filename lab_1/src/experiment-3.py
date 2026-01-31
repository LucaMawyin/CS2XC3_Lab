import bad_sorts

import time
from math import *
import matplotlib.pyplot as plt


def run():
    algorithms = [
        (bad_sorts.insertion_sort, "Insertion Sort"),
        (bad_sorts.bubble_sort, "Bubble Sort"),
        (bad_sorts.selection_sort, "Selection Sort")
    ]
    
    length = 2000
    swaps = int(length*log2(length) / 2)
    #print(swaps)
    #quit()
    rng = range(0, swaps,100) 
    time_factor = 1000 # seconds -> milliseconds

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing",label,"...")
        for i in rng:
            #print(i/swaps * 100)
            L = bad_sorts.create_near_sorted_list(length, 100000,i)
            
            start = time.perf_counter() * time_factor
            sort_func(L)
            end = time.perf_counter() * time_factor
            
            runtimes.append(end - start)
        
        plt.plot(rng, runtimes, label=label)
        

    plt.title("Sorting Algorithm Performance Comparison on Sorted Lists with varying numbers of Swaps")
    #plt.yscale('log')
    plt.xlabel("Number of Swaps")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    



if __name__ == '__main__':
    run()
