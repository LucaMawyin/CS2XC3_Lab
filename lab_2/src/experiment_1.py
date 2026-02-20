from graph import *
import matplotlib.pyplot as plt

NODE_AMOUNT = 100
EDGE_AMOUNT_MAX = 100
EDGE_AMOUNT_STEP = 1
TEST_AMOUNT = 1000
edge_amounts = [i for i in range(0,EDGE_AMOUNT_MAX,EDGE_AMOUNT_STEP)]
probabilities = [0 for _ in range(0,EDGE_AMOUNT_MAX,EDGE_AMOUNT_STEP)]


for i,ea in enumerate(edge_amounts):
    probability = 0
    print(f"{(i/len(edge_amounts)*100):0.2f}%")
    for _ in range(TEST_AMOUNT):
        graph = create_random_graph(NODE_AMOUNT,ea)
        probability += 1 if has_cycle(graph) else 0
    probability /= TEST_AMOUNT
    probability *= 100

    probabilities[i] = probability
            

# Create the plot
plt.plot(edge_amounts, probabilities)
plt.title(f'Probabilties of cycles existing in graphs with {NODE_AMOUNT} nodes')
plt.xlabel('Number of edges')
plt.ylabel('% chance there is a cycle')
plt.grid(True)

plt.show()