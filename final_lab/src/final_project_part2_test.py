from final_project_part2 import *
from math import sqrt


# this graph used for testing comes from the Computerphile video mentioned in the assignment instructions:
# https://www.youtube.com/watch?v=ySN5Wnu88nE&t=359s

posses = {
    "S": (3.0, 9.0),
    "A": (1.0, 7.0),
    "B": (3.5, 6.5),
    "C": (7.0, 8.5),
    "D": (2.0, 4.5),
    "H": (4.0, 4.5),
    "F": (3.0, 2.0),
    "G": (5.5, 3.0),
    "L": (8.5, 6.0),
    "I": (7.5, 4.5),
    "J": (9.5, 4.5),
    "K": (8.5, 3.0),
    "E": (8.0, 1.0)
}
nodes = list(posses.keys())


def calc_h(node):
    out_dict = {}
    sx, sy = posses[node]
    for onode in posses:
        ox, oy = posses[onode]
        dist = sqrt((sx - ox)**2 + (sy - oy)**2)
        out_dict[onode] = dist * 0.5

    return out_dict


g = DirectedWeightedGraph()
for x in nodes:
    g.add_node(x)

edge_list = [
    ("S", "A", 7), ("S", "B", 2), ("S", "C", 3), ("A", "B", 3),
    ("A", "D", 4), ("B", "D", 4), ("B", "H", 1), ("C", "L", 2),
    ("D", "F", 5), ("H", "F", 3), ("H", "G", 2), ("G", "E", 2),
    ("L", "I", 4), ("L", "J", 4), ("I", "J", 6), ("I", "K", 4),
    ("J", "K", 4), ("K", "E", 5),
]

for node1, node2, weight in edge_list:
    g.add_edge(node1, node2, weight)
    g.add_edge(node2, node1, weight)

if __name__ == "__main__":
    for x in nodes:
        for y in nodes:
            # print(x, y)
            _, dist = a_star(g, x, y, calc_h(y))
            _, dists_map = dijkstra(g, x)
            # print(dists_map)
            assert dist == dists_map[y], f"failed on {x} -> {y}: {dist} != {dists_map[y]}"

    print("done")
