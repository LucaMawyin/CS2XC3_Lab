import random
from bst import BST
from lab3 import RBTree

# For trees from lists of length 10000
trials = 1000
size = 10000
bst_total = 0
rbt_total = 0
average_difference = 0
for _ in range(trials):

    numbers = random.sample(range(1000000), size)

    bst = BST()
    rbt = RBTree()

    for n in numbers:
        bst.insert(n)
        rbt.insert(n)
    
    bst_total += bst.height()
    rbt_total += rbt.get_height()
    average_difference += bst.height() - rbt.get_height()
    print("BST height:", bst.height())
    print("RBT height:", rbt.get_height())
    print()

print("Average BST height:", bst_total / trials)
print("Average RBT height:", rbt_total / trials)
print("Average height difference:", average_difference / trials)
