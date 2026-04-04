from final_project_part1_approx import *
from final_project_part1 import *
import matplotlib.pyplot as plt
import random

def create_random_sparse_graph(n, upper, p):
    G = DirectedWeightedGraph()

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j, random.randint(1, upper))

    return G

# Testing dijkstra_approx and bellman_ford_approx for increasing k

number_of_nodes = 1000
source = 0

k_values = []
dijkstra_errors = []
bellman_ford_errors = []

G = create_random_sparse_graph(number_of_nodes, 100, p=0.05)

true_dijkstra = total_dist(dijkstra(G, source))
true_bellman_ford = total_dist(bellman_ford(G, source))

for k in range(1,21):

    approx_dijkstra = total_dist(dijkstra_approx(G, source, k))
    approx_bellman_ford = total_dist(bellman_ford_approx(G, source, k))

    d_error = abs(true_dijkstra - approx_dijkstra)
    b_error = abs(true_bellman_ford - approx_bellman_ford)

    k_values.append(k)
    dijkstra_errors.append(d_error)
    bellman_ford_errors.append(b_error)

plt.plot(k_values, dijkstra_errors, label='Dijkstra Approx Error', marker='o')
plt.plot(k_values, bellman_ford_errors, label='Bellman-Ford Approx Error', marker='s')

plt.xticks(range(0,21,2))
plt.xlabel('k')
plt.ylabel('Total Distance Error')
plt.title('Total Distance Error vs k (Sparse Graph)')
plt.legend()
plt.show()