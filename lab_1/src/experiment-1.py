import bad_sorts
import good_sorts

import time
import matplotlib.pyplot as plt


def run():
    algorithms = [
        (bad_sorts.insertion_sort, "Insertion Sort"),
        (bad_sorts.bubble_sort, "Bubble Sort"),
        (bad_sorts.selection_sort, "Selection Sort"),
        (good_sorts.quicksort, "Quick Sort"),
        (good_sorts.mergesort, "Merge Sort"),
        (good_sorts.heapsort, "Heap Sort")
    ]
    
    rng = range(0, 1000,10) 
    
    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing",label,"...")
        for i in rng:
            L = bad_sorts.create_random_list(i, 100000)
            
            start = time.perf_counter()
            sort_func(L)
            end = time.perf_counter()
            
            runtimes.append(end - start)
        
        plt.plot(rng, runtimes, label=label)
        

    plt.title("Sorting Algorithm Performance Comparison")
    plt.yscale('log')
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    



if __name__ == '__main__':
    run()
