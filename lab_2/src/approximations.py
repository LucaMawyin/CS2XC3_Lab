from graph import *

# NOTE: GRAPH IS A DICTIONARY

def approx1(G:Graph):

    highestDegreeVertex = None
    highestDegree = -1

    for node in G.adj:
        currentNodeDegree = len(G.adj[node])
        if currentNodeDegree > highestDegree:
            highestDegree = currentNodeDegree
            highestDegreeVertex = node

    return "TODO: Implement approx1"

def approx2(G:Graph):
    return "TODO: Implement approx2"

def approx3(G:Graph):
    return "TODO: Implement approx3"