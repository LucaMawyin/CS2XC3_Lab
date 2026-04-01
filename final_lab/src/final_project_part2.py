import min_heap
from final_project_part1 import *


class AStarElement(min_heap.Element):
    def __init__(self, value, key, h_val):
        super().__init__(value, key)
        self.h_val = h_val

    @property
    def key(self):
        return self.h_val + self._key

    @key.setter
    def key(self, value):
        self._key = value

    def __str__(self):
        return f"({self.value}, {self.h_val}, {self._key} | {self.key})"


def a_star(G: DirectedWeightedGraph, s, d, h):
    pred = {}  # Predecessor dictionary
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap with their keys and heuristic values
    for node in nodes:
        Q.insert(AStarElement(node, float("inf"), h[node]))
        dist[node] = float("inf")

    Q.decrease_key(s, 0)
    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element._key

        if current_node == d:
            return pred, dist[current_node]

        for neighbour in G.adj[current_node]:
            if neighbour not in Q.map: continue
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node

    return pred, float("inf")



