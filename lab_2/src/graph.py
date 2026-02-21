from collections import deque
import math
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

####################################################
#             Pre PART 1 Implementation            #
####################################################


def BFS2(G, node1, node2):
    Q = deque([[node1]])
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True

    while len(Q) != 0:
        current_path = Q.popleft()
        current_node = current_path[-1]
        for node in G.adj[current_node]:
            if node == node2:
                return current_path + [node]
            if not marked[node]:
                Q.append(current_path + [node])
                marked[node] = True
    return []

def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True

    while len(S) != 0:
        current_node = S[-1]
        if current_node == node2:
                return S
        
        found = False
        for node in G.adj[current_node]:
            if marked[node]: continue
            S.append(node)
            marked[node] = True
            found = True
            break
        
        if not found:
            S.pop() 

    return []

def BFS3(G,node1):
    Q = deque([node1])
    marked = {node1 : True}
    predecessor = {}

    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predecessor[node] = current_node

    return predecessor

def DFS3(G,node1):
    S = [node1]
    marked = {}
    predecessor = {}

    for node in G.adj:
        marked[node] = False
    
    
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)
                if not marked[node] and not node in predecessor:
                    predecessor[node] = current_node

    return predecessor

# TODO: is this right? since it's undirected isn't there being an edge mean it has a cycle (you can just go to a node and back)
def has_cycle(G):
    marked = {}
    for node in G.adj:
        marked[node] = False

    def BFS3(node1):
        nonlocal marked,G

        Q = deque([node1])
        marked[node1] = True
        parent_node = node1
        current_node = node1

        while len(Q) != 0:
            parent_node = current_node
            current_node = Q.popleft()
            for node in G.adj[current_node]:
                if node == parent_node: continue

                if marked[node]:
                    return True
                else:
                    Q.append(node)
                    marked[node] = True

        return False

    for node in G.adj:
        if marked[node]: continue
        if BFS3(node): return True
    
    return False

        


def is_connected(G):
    return len(BFS3(G,next(iter(G.adj)))) >= len(G.adj) - 1


#######################################
#             Experiment 1            #
#######################################

def create_random_graph(i, j):
    graph = Graph(i)
    MAX_EDGES = i * (i - 1)//2

    if j > MAX_EDGES: 
        print("Maxxed out at",j)
        j = MAX_EDGES

    selected_indices = random.sample(range(MAX_EDGES), j)
    
    
    for k in selected_indices:
        u = i - 2 - int(math.floor((math.sqrt(-8*k + 4*i*(i-1)-7) / 2.0) - 0.5))
        v = k + u + 1 - i*(i-1)//2 + (i-u)*(i-u-1)//2
        graph.add_edge(u, v)

    return graph






#TODO: Probably should delete when we're done
### Test

if __name__ == "__main__":
    print("Running Tests")

    G = Graph(6)
    for u, v in [
        (0, 1), # 1 to 2
        (0, 2), # 1 to 3
        (1, 3), # 2 to 4
        (2, 3), # 3 to 4
        (2, 4), # 3 to 5
        (3, 4), # 4 to 5
        (3, 5)  # 4 to 6
    ]:
        G.add_edge(u, v)

    path = BFS2(G, 0, 5)
    assert path in (
        [0,1,3,5],
        [0,2,3,5]
    ), print(path)

    path = DFS2(G, 0, 5)
    assert path in (
        [0,1,3,5],
        [0,2,3,5],
        [0,2,4,3,5]
    ), print(path)
    
    pred = BFS3(G,0)
    assert pred in (
        {1 : 0, 2 : 0, 3 : 1, 4 : 2, 5 : 3},
        {1 : 0, 2 : 0, 3 : 2, 4 : 2, 5 : 3}
    ), print(pred)

    print(DFS3(G,0))

    assert has_cycle(G)

    G1 = Graph(4)
    G1.add_edge(1,2)
    assert not has_cycle(G1)
    G1.add_edge(2,3)
    assert not has_cycle(G1)
    G1.add_edge(1,3)
    assert has_cycle(G1)


    G3 = Graph(100)
    for i in range(99):
        G3.add_edge(i,i+1)
    assert not has_cycle(G3)
    G3.add_edge(99,0)
    assert has_cycle(G3)
    

    G2 = Graph(2)
    assert not is_connected(G2)
    G2.add_edge(0,1)
    assert is_connected(G2)
    G2.add_node()
    assert not is_connected(G2)

    print("Passed Tests")
    