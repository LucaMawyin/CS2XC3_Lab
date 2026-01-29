import bad_sorts
import time
import matplotlib.pyplot as plt
import numpy as np
import random


def run():
    runtimes = []
    
    rng = range(0,1000,10)
    for i in rng:
        L = bad_sorts.create_random_list(i, 100000)
        start = time.perf_counter()
        bad_sorts.insertion_sort(L)
        end = time.perf_counter()

        runtimes.append(end - start)

    plt.plot(rng, runtimes)
    plt.xlabel("Run number")
    plt.ylabel("Time (seconds)")
    plt.show()



if __name__ == '__main__':
    run()
