from graph import *
from approximations import *
import matplotlib.pyplot as plt

numberOfGraphs = 1000
numberOfNodesInGraph = 8
numberOfEdgesInGraph = [1] + list(range(5, 31, 5))

results = {}

for edgeLength in numberOfEdgesInGraph:
    mvcSum = 0
    approx1Sum = 0
    approx2Sum = 0
    approx3Sum = 0

    for _ in range(numberOfGraphs):
        G = create_random_graph2(numberOfNodesInGraph, edgeLength)
        mvcSum += len(MVC(G))
        approx1Sum += len(approx1(G))
        approx2Sum += len(approx2(G))
        approx3Sum += len(approx3(G))
    
    results[edgeLength] = {
        "MVC" : mvcSum,
        "approx1" : approx1Sum,
        "approx2" : approx2Sum,
        "approx3" : approx3Sum
    }


listOfEdgesInGraphs = list(results.keys())
mvcSumList = [results[edgeLength]["MVC"] for edgeLength in listOfEdgesInGraphs]
approx1SumList = [results[edgeLength]["approx1"] for edgeLength in listOfEdgesInGraphs]
approx2SumList = [results[edgeLength]["approx2"] for edgeLength in listOfEdgesInGraphs]
approx3SumList = [results[edgeLength]["approx3"] for edgeLength in listOfEdgesInGraphs]

plt.figure(figsize=(10,6))
plt.plot(listOfEdgesInGraphs, mvcSumList, label="MVC")
plt.plot(listOfEdgesInGraphs, approx1SumList, label="approx1")
plt.plot(listOfEdgesInGraphs, approx2SumList, label="approx2")
plt.plot(listOfEdgesInGraphs, approx3SumList, label="approx3")

plt.xlabel("Number of Edges in Graph")
plt.ylabel("Sum of Vertex Cover Sized")
plt.title("Vertex Cover Size vs Number of Edges on 1000 Graphs")
plt.legend()
plt.grid(True)
plt.show()