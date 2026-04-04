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

# Testing dijkstra_approx and bellman_ford_approx for edges

source = 0

p=0.05
n_values = [i for i in range(100,500,50)]
k_values = [1,3,5]

d_scores = {k: [] for k in k_values}
b_scores = {k: [] for k in k_values}

for k in k_values:
    for n in n_values:
        G = create_random_sparse_graph(n, 100, p)
        
        true_dijkstra = total_dist(dijkstra(G, source))
        true_bellman_ford = total_dist(bellman_ford(G, source))

        approx_dijkstra = total_dist(dijkstra_approx(G, source, k))
        approx_bellman_ford = total_dist(bellman_ford_approx(G, source, k))

        d_score = abs(true_dijkstra - approx_dijkstra) / n
        b_score = abs(true_bellman_ford - approx_bellman_ford) / n

        d_scores[k].append(d_score)
        b_scores[k].append(b_score)


for k in k_values:
    plt.plot(n_values, d_scores[k], label=f'Dijkstra Approx (k={k})', marker='o')
    plt.plot(n_values, b_scores[k], label=f'Bellman-Ford Approx (k={k})', marker='s')

plt.xlabel('Graph Size (Number of Nodes)')
plt.ylabel('Relative Distance Error (Approx)')
plt.title('Relative Distance Error vs Graph Size (Sparse Graph)')
plt.legend(loc="center left")
plt.show()