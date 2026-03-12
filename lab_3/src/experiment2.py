import matplotlib.pyplot as plt
import random
from sorting import *
from rbt import *
from bst import *
import sys
sys.setrecursionlimit(20000)

listOfNumbers = []
size = 1000
trials = 5
swaps_list = []
avg_diffs = []

# Generating 200 sorted lists of length 10 000
for i in range(200):
    numberOfSwaps = i * 5
    total_diff = 0
    for _ in range(trials):
        lst = create_near_sorted_list(size, 100000, numberOfSwaps)

        rbt = RBTree()
        bst = BST()

        for elem in lst:
            rbt.insert(elem)
            bst.insert(elem)

        bstHeight = bst.height()
        rbtHeight = rbt.get_height()

        total_diff += (bstHeight - rbtHeight)

    avg_diff = total_diff / trials
    swaps_list.append(numberOfSwaps)
    avg_diffs.append(avg_diff)

plt.plot(swaps_list, avg_diffs)
plt.xlabel("Number of Swaps")
plt.ylabel("Average Height Difference (BST - RBT)/Trials")
plt.title("Average Height Difference vs Number of Swaps in Near Sorted List")
plt.show()
