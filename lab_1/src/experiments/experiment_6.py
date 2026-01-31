from sorting import bad_sorts as bs
from sorting import good_sorts as gs

import time
import matplotlib.pyplot as plt


def run():
    algorithms = [
        (gs.quicksort_copy, "Quick Sort"),
        (gs.dual_quicksort, "Dual Quick Sort"),
    ]
    
    rng = range(0, 1000,10) 
    time_factor = 1000 # seconds -> milliseconds
    avg_run = 5

    plt.figure(figsize=(10, 6))

    for sort_func, label in algorithms:
        runtimes = []
        print("testing",label,"...")
        for i in rng:
            total_time = 0
            for _ in range(avg_run):

                L = bs.create_random_list(i, 100000)
                
                start = time.perf_counter()
                sort_func(L)
                end = time.perf_counter()

                total_time += end - start
            
            runtimes.append((total_time/avg_run) * time_factor)
        
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
