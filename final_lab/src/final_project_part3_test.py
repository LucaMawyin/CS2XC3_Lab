from final_project_part3 import *
def test_load_london_data():
    # Make sure the graph and metadata load correctly
    G, stations, edge_lines = load_london_data()

    assert G.number_of_nodes() > 0
    assert len(stations) > 0
    assert len(edge_lines) > 0

    print("test_load_london_data passed")

def test_sample_pairs():
    # Compare A* and Dijkstra on a few sample station pairs
    G, stations, edge_lines = load_london_data()
    nodes = list(stations.keys())

    sample_pairs = [
        (nodes[0], nodes[10]),
        (nodes[5], nodes[25]),
        (nodes[20], nodes[50]),
    ]

    for s, d in sample_pairs:
        h = calc_h(d, stations)

        _, d_dist, _ = dijkstra_to_dest(G, s, d)
        _, a_dist = a_star(G, s, d, h)

        assert abs(d_dist - a_dist) < 1e-9, f"Mismatch on {s} -> {d}"

    print("test_sample_pairs passed")

def test_many_pairs(limit=200):
    # Compare A* and Dijkstra on many pairs to verify correctness
    G, stations, edge_lines = load_london_data()
    nodes = list(stations.keys())

    count = 0
    for s in nodes:
        for d in nodes:
            if s == d:
                continue

            h = calc_h(d, stations)

            _, d_dist, _ = dijkstra_to_dest(G, s, d)
            _, a_dist = a_star(G, s, d, h)

            assert abs(d_dist - a_dist) < 1e-9, f"Mismatch on {s} -> {d}"

            count += 1
            if count >= limit:
                print("test_many_pairs passed")
                return
            
if __name__ == "__main__":
    test_load_london_data()
    test_sample_pairs()
    test_many_pairs()
    print("All Part 3 tests passed")