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

number_of_nodes = 500
source = 0

p_values = [(i*0.01) for i in range(1,11)]
k_values = [2,5,10]

d_scores = {k: [] for k in k_values}
b_scores = {k: [] for k in k_values}

for k in k_values:
    for p in p_values:
        G = create_random_sparse_graph(number_of_nodes, 10, p)
        
        true_dijkstra = total_dist(dijkstra(G, source))
        true_bellman_ford = total_dist(bellman_ford(G, source))

        approx_dijkstra = total_dist(dijkstra_approx(G, source, k))
        approx_bellman_ford = total_dist(bellman_ford_approx(G, source, k))

        d_score = abs(true_dijkstra - approx_dijkstra)
        b_score = abs(true_bellman_ford - approx_bellman_ford)

        d_scores[k].append(d_score)
        b_scores[k].append(b_score)


for k in k_values:
    plt.plot(p_values, d_scores[k], label=f'Dijkstra Approx Score (k={k})', marker='o')
    plt.plot(p_values, b_scores[k], label=f'Bellman-Ford Approx Score (k={k})', marker='s')

plt.xlabel('Graph Density (p)')
plt.ylabel('Total Distance Error (approx)')
plt.title('Total Distance Error vs Graph Density (Sparse Graph)')
plt.legend()
plt.show()