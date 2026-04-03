import csv
import math

# Check whether Dijkstra and A* produced the same shortest-path distance
bad_rows = []

with open("part3_results.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        d1 = float(row["dijkstra_distance"])
        d2 = float(row["astar_distance"])
        if abs(d1 - d2) > 1e-9:
            bad_rows.append((row["source"], row["destination"], d1, d2))

print("Number of mismatches:", len(bad_rows))
if bad_rows:
    print("First few mismatches:", bad_rows[:10])


# Check for invalid rows such as infinite distance or empty reconstructed path
bad = []

with open("part3_results.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dist = float(row["dijkstra_distance"])
        path_len = int(row["path_length"])
        if math.isinf(dist) or path_len == 0:
            bad.append((row["source"], row["destination"], dist, path_len))

print("Bad rows:", len(bad))
print(bad[:10])