import final_project_part1 as p1
import final_project_part2 as p2
import min_heap


class Graph():
    def __init__(self):
        self.adj = {}

    def get_adj_nodes(self, node: int) -> list[int]:
        return self.adj[node]

    def add_node(self, node: int):
        self.adj[node] = []

    def add_edge(self, node1: int, node2: int):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)

    def get_num_of_nodes(self) -> int:
        return len(self.adj)


class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()
        self.weights = {}

    def add_edge(self, node1: int, node2: int, w: float):
        super().add_edge(node1, node2)
        self.weights[(node1, node2)] = w

    def w(self, node1: int, node2: int) -> float:
        return self.weights[(node1, node2)]


class HeuristicGraph(WeightedGraph):
    def __init__(self, heuristic_dict: dict[int, float]):
        super().__init__()
        self.heuristic = heuristic_dict

    def get_heuristic(self) -> dict[int, float]:
        return self.heuristic


class SPAlgorithm:
    @staticmethod
    def calc_sp(graph, source, dest) -> float:
        pass


class Dijkstra(SPAlgorithm):
    @staticmethod
    def calc_sp(graph, source, dest) -> float:
        assert isinstance(graph, WeightedGraph)

        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = min_heap.MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        # Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key

            if current_node == dest:
                return dist[current_node]

            for neighbour in graph.adj[current_node]:
                if neighbour not in Q.map:
                    continue
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node

        return float("inf")


class Bellman_Ford(SPAlgorithm):
    @staticmethod
    def calc_sp(graph, source, dest) -> float:
        assert isinstance(graph, WeightedGraph)
        inp_graph = p1.DirectedWeightedGraph()
        inp_graph.adj = graph.adj
        inp_graph.weights = graph.weights
        out = p1.bellman_ford(inp_graph, source)
        return out[dest]


class A_Star(SPAlgorithm):
    @staticmethod
    def calc_sp(graph, source, dest) -> float:
        assert isinstance(graph, HeuristicGraph)
        inp_graph = p1.DirectedWeightedGraph()
        inp_graph.adj = graph.adj
        inp_graph.weights = graph.weights
        _, out = p2.a_star(inp_graph, source, dest, graph.get_heuristic())
        return out
