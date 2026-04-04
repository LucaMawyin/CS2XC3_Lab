import csv
import math
import time
from collections import defaultdict

from final_project_part1 import DirectedWeightedGraph
from final_project_part2 import a_star
import min_heap

def haversine(lat1, lon1, lat2, lon2):
    # Return the great-circle distance between two coordinates in kilometers
    R = 6371.0

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )

    return 2 * R * math.asin(math.sqrt(a))

def load_london_data(
    stations_file="london_stations.csv",
    connections_file="london_connections.csv",
):
    # Load station metadata indexed by station id
    stations = {}

    with open(stations_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            station_id = int(row["id"])
            stations[station_id] = {
                "name": row["name"],
                "lat": float(row["latitude"]),
                "lon": float(row["longitude"]),
            }

    # Build the weighted graph
    G = DirectedWeightedGraph()
    for station_id in stations:
        G.add_node(station_id)

    # Store line information so we can analyze transfers later
    edge_lines = defaultdict(set)

    with open(connections_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            u = int(row["station1"])
            v = int(row["station2"])
            line = int(row["line"])

            weight = haversine(
                stations[u]["lat"], stations[u]["lon"],
                stations[v]["lat"], stations[v]["lon"]
            )

            # Treat the Tube connection as bidirectional
            if not G.are_connected(u, v):
                G.add_edge(u, v, weight)
            if not G.are_connected(v, u):
                G.add_edge(v, u, weight)

            edge_lines[(u, v)].add(line)
            edge_lines[(v, u)].add(line)

    return G, stations, edge_lines

def calc_h(dest, stations):
    # Build a heuristic dictionary for a fixed destination
    h = {}

    dest_lat = stations[dest]["lat"]
    dest_lon = stations[dest]["lon"]

    for node in stations:
        h[node] = haversine(
            stations[node]["lat"], stations[node]["lon"],
            dest_lat, dest_lon
        )

    return h

def dijkstra_to_dest(G, s, d):
    # Run Dijkstra until the destination is extracted from the heap
    pred = {}
    dist = {}
    Q = min_heap.MinHeap([])

    nodes = list(G.adj.keys())

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")

    Q.decrease_key(s, 0)

    visited_count = 0

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        visited_count += 1

        if current_node == d:
            return pred, dist[current_node], visited_count

        for neighbour in G.adj[current_node]:
            if neighbour not in Q.map:
                continue

            new_dist = dist[current_node] + G.w(current_node, neighbour)
            if new_dist < dist[neighbour]:
                Q.decrease_key(neighbour, new_dist)
                dist[neighbour] = new_dist
                pred[neighbour] = current_node

    return pred, float("inf"), visited_count

def reconstruct_path(pred, s, d):
    # Rebuild the path from s to d using the predecessor dictionary
    if s == d:
        return [s]

    if d not in pred:
        return []

    path = [d]
    current = d

    while current != s:
        current = pred[current]
        path.append(current)

    path.reverse()
    return path
def min_transfers(path, edge_lines):
    # Return the minimum number of line changes along the path
    if len(path) < 2:
        return 0

    current_lines = {line: 0 for line in edge_lines[(path[0], path[1])]}

    for i in range(1, len(path) - 1):
        next_lines = edge_lines[(path[i], path[i + 1])]
        next_costs = {}

        for new_line in next_lines:
            best = float("inf")
            for old_line, old_cost in current_lines.items():
                extra = 0 if old_line == new_line else 1
                best = min(best, old_cost + extra)
            next_costs[new_line] = best

        current_lines = next_costs

    return min(current_lines.values())

def run_experiment(
    G,
    stations,
    edge_lines,
    output_file="part3_results.csv",
    max_pairs=None,
    progress_interval=1000,
):
    # Run Dijkstra and A* on many source-destination pairs and save the results
    nodes = list(stations.keys())
    pair_count = 0
    heuristic_cache = {}

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "source",
            "destination",
            "dijkstra_distance",
            "astar_distance",
            "dijkstra_time_ns",
            "astar_time_ns",
            "dijkstra_visited",
            "path_length",
            "transfers",
        ])

        for d in nodes:
            if d not in heuristic_cache:
                heuristic_cache[d] = calc_h(d, stations)

            h = heuristic_cache[d]

            for s in nodes:
                if s == d:
                    continue

                start = time.perf_counter_ns()
                d_pred, d_dist, d_visited = dijkstra_to_dest(G, s, d)
                d_time = time.perf_counter_ns() - start

                start = time.perf_counter_ns()
                a_pred, a_dist = a_star(G, s, d, h)
                a_time = time.perf_counter_ns() - start

                path = reconstruct_path(d_pred, s, d)
                transfers = min_transfers(path, edge_lines)

                writer.writerow([
                    s,
                    d,
                    d_dist,
                    a_dist,
                    d_time,
                    a_time,
                    d_visited,
                    len(path),
                    transfers,
                ])

                pair_count += 1

                if progress_interval is not None and pair_count % progress_interval == 0:
                    print(f"Processed {pair_count} pairs...", flush=True)

                if max_pairs is not None and pair_count >= max_pairs:
                    return

if __name__ == "__main__":
    G, stations, edge_lines = load_london_data()
    run_experiment(G, stations, edge_lines, max_pairs=None)
    print("part3_results.csv has been generated.")