from final_project_part1 import *
import min_heap

def dijkstra_approx(G, source, k):
    '''
    # Dijkstra's algorithm which relax each node at most k times.

    # Returns a distance dictionary which maps a node (integer) to the distance 
    # of the shortest path known to the node (based off the approximation).     
    '''

    distance_dict = {}
    relax_count = {}
    Q = min_heap.MinHeap([])

    for node in G.adj.keys():
        distance_dict[node] = float("inf")
        relax_count[node] = 0
        Q.insert(min_heap.Element(node, float("inf")))

    Q.decrease_key(source, 0)
    distance_dict[source] = 0

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value

        if current_element.key != distance_dict[current_node]:
            continue

        for neighbour in G.adj[current_node]:

            new_distance = distance_dict[current_node] + G.w(current_node, neighbour)
            
            if new_distance < distance_dict[neighbour] and relax_count[neighbour] < k:
                distance_dict[neighbour] = new_distance
                relax_count[neighbour] += 1
                Q.decrease_key(neighbour, new_distance)

    return distance_dict    

def bellman_ford_approx(G, source, k):
    '''
    # Bellman-Ford's algorithm which relax each node at most k times.

    # Returns a distance dictionary which maps a node (integer) to the distance 
    # of the shortest path known to the node (based off the approximation).     
    '''

    distance_dict = {}

    for node in G.adj.keys():
        distance_dict[node] = float("inf")

    distance_dict[source] = 0

    for _ in range(k):
        for node in G.adj.keys():
            for neighbour in G.adj[node]:
                new_distance = distance_dict[node] + G.w(node, neighbour)
                if new_distance < distance_dict[neighbour]:
                    distance_dict[neighbour] = new_distance

    return distance_dict