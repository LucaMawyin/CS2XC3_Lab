from graph import *
import random

# NOTE: All algorithms assume every node in graph has at least 1 edge

def approx1(G:Graph):

    graphCopy = copyGraph(G)
    C = set()

    while not is_vertex_cover(G, C):
        highestDegreeVertex = findHighestDegreeVertex(graphCopy)
        C.add(highestDegreeVertex)

        for neighbouringNode in graphCopy.adj[highestDegreeVertex]:
            graphCopy.adj[neighbouringNode].remove(highestDegreeVertex)
        graphCopy.adj[highestDegreeVertex] = []

    return C

def approx2(G:Graph):

    C = set()

    listOfNodes = list(G.adj.keys())
    shuffledListOfNodes = random.sample(listOfNodes, len(listOfNodes))

    while not is_vertex_cover(G,C):
        C.add(shuffledListOfNodes.pop())

    return C

def approx3(G:Graph):

    graphCopy = copyGraph(G)
    C = set()

    while not is_vertex_cover(G,C) and (
            any(len(graphCopy.adj[node]) > 0 for node in graphCopy.adj)
        ):
        
        nodesWithEdges = [node for node in graphCopy.adj if len(graphCopy.adj[node]) > 0]
        randomNodeWithEdges = random.choice(nodesWithEdges)
        randomNodeNeighbour = random.choice(graphCopy.adj[randomNodeWithEdges])

        C.add(randomNodeWithEdges)
        C.add(randomNodeNeighbour)

        for neighbouringNode in graphCopy.adj[randomNodeWithEdges]:
            graphCopy.adj[neighbouringNode].remove(randomNodeWithEdges)

        for neighbouringNode in graphCopy.adj[randomNodeNeighbour]:
            graphCopy.adj[neighbouringNode].remove(randomNodeNeighbour)
        
        graphCopy.adj.pop(randomNodeWithEdges)
        graphCopy.adj.pop(randomNodeNeighbour)

    return C

def findHighestDegreeVertex(G:Graph):
    highestDegreeVertex = None
    highestDegree = -1

    for node in G.adj:
        currentNodeDegree = len(G.adj[node])
        if currentNodeDegree > highestDegree:
            highestDegree = currentNodeDegree
            highestDegreeVertex = node

    return highestDegreeVertex

def copyGraph(G:Graph):
    graphCopy = Graph(len(G.adj))

    for node in G.adj:
        graphCopy.adj[node] = G.adj[node].copy()

    return graphCopy