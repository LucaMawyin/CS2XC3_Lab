import csv
import math
import matplotlib.pyplot as plt


def load_results(filename="part3_results.csv"):
    # Load experiment results from the CSV file
    rows = []

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "source": int(row["source"]),
                "destination": int(row["destination"]),
                "dijkstra_distance": float(row["dijkstra_distance"]),
                "astar_distance": float(row["astar_distance"]),
                "dijkstra_time_ns": int(row["dijkstra_time_ns"]),
                "astar_time_ns": int(row["astar_time_ns"]),
                "dijkstra_visited": int(row["dijkstra_visited"]),
                "path_length": int(row["path_length"]),
                "transfers": int(row["transfers"]),
            })

    return rows


def median(values):
    # Return the median of a list of numeric values
    values = sorted(values)
    n = len(values)

    if n == 0:
        return 0

    mid = n // 2

    if n % 2 == 1:
        return values[mid]

    return (values[mid - 1] + values[mid]) / 2


def transfer_category(transfers):
    # Group transfer counts into broader categories for easier analysis
    if transfers == 0:
        return "Same line"
    if transfers == 1:
        return "One transfer"
    return "Several transfers"


def plot_runtime_comparison(rows, save_path="Final_project_part3_Figure_1.png"):
    # Plot a downsampled runtime comparison between Dijkstra and A*
    dijkstra_times = [row["dijkstra_time_ns"] for row in rows]
    astar_times = [row["astar_time_ns"] for row in rows]

    total_points = len(rows)
    step = max(1, total_points // 2000)

    sampled_indices = list(range(0, total_points, step))
    sampled_dijkstra = [dijkstra_times[i] for i in sampled_indices]
    sampled_astar = [astar_times[i] for i in sampled_indices]

    plt.figure(figsize=(10, 6))
    plt.plot(sampled_indices, sampled_dijkstra, label="Dijkstra")
    plt.plot(sampled_indices, sampled_astar, label="A*")
    plt.xlabel("Pair index")
    plt.ylabel("Runtime (ns)")
    plt.title("Dijkstra vs A* Runtime (Downsampled)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()


def plot_runtime_by_transfers(rows, save_path="Final_project_part3_Figure_2.png"):
    # Plot median runtime by exact number of transfers
    grouped = {}

    for row in rows:
        transfers = row["transfers"]
        if transfers not in grouped:
            grouped[transfers] = {"d": [], "a": []}

        grouped[transfers]["d"].append(row["dijkstra_time_ns"])
        grouped[transfers]["a"].append(row["astar_time_ns"])

    transfer_values = sorted(grouped.keys())
    d_median = [median(grouped[t]["d"]) for t in transfer_values]
    a_median = [median(grouped[t]["a"]) for t in transfer_values]

    plt.figure(figsize=(8, 5))
    plt.plot(transfer_values, d_median, marker="o", label="Dijkstra")
    plt.plot(transfer_values, a_median, marker="o", label="A*")
    plt.xlabel("Number of transfers")
    plt.ylabel("Median runtime (ns)")
    plt.title("Median Runtime by Transfers")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()


def plot_runtime_by_transfer_category(
    rows,
    save_path="Final_project_part3_Figure_3.png"
):
    # Plot median runtime by broader transfer categories
    grouped = {
        "Same line": {"d": [], "a": []},
        "One transfer": {"d": [], "a": []},
        "Several transfers": {"d": [], "a": []},
    }

    for row in rows:
        category = transfer_category(row["transfers"])
        grouped[category]["d"].append(row["dijkstra_time_ns"])
        grouped[category]["a"].append(row["astar_time_ns"])

    categories = ["Same line", "One transfer", "Several transfers"]
    d_median = [median(grouped[c]["d"]) for c in categories]
    a_median = [median(grouped[c]["a"]) for c in categories]

    x = range(len(categories))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width / 2 for i in x], d_median, width=width, label="Dijkstra")
    plt.bar([i + width / 2 for i in x], a_median, width=width, label="A*")
    plt.xticks(list(x), categories)
    plt.xlabel("Transfer category")
    plt.ylabel("Median runtime (ns)")
    plt.title("Median Runtime by Transfer Category")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()


def plot_runtime_by_path_length(
    rows,
    save_path="Final_project_part3_Figure_4.png"
):
    # Plot median runtime by shortest path length
    grouped = {}

    for row in rows:
        path_length = row["path_length"]
        if path_length not in grouped:
            grouped[path_length] = {"d": [], "a": []}

        grouped[path_length]["d"].append(row["dijkstra_time_ns"])
        grouped[path_length]["a"].append(row["astar_time_ns"])

    path_lengths = sorted(grouped.keys())
    d_median = [median(grouped[length]["d"]) for length in path_lengths]
    a_median = [median(grouped[length]["a"]) for length in path_lengths]

    plt.figure(figsize=(8, 5))
    plt.plot(path_lengths, d_median, marker="o", label="Dijkstra")
    plt.plot(path_lengths, a_median, marker="o", label="A*")
    plt.xlabel("Shortest path length")
    plt.ylabel("Median runtime (ns)")
    plt.title("Median Runtime by Path Length")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()


def plot_speedup_by_transfer_category(
    rows,
    save_path="Final_project_part3_Figure_5.png"
):
    # Plot the median Dijkstra/A* speedup by transfer category
    grouped = {
        "Same line": [],
        "One transfer": [],
        "Several transfers": [],
    }

    for row in rows:
        if row["astar_time_ns"] == 0:
            continue

        category = transfer_category(row["transfers"])
        speedup = row["dijkstra_time_ns"] / row["astar_time_ns"]
        grouped[category].append(speedup)

    categories = ["Same line", "One transfer", "Several transfers"]
    speedups = [median(grouped[c]) for c in categories]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, speedups)
    plt.xlabel("Transfer category")
    plt.ylabel("Median speedup (Dijkstra / A*)")
    plt.title("A* Speedup by Transfer Category")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()


if __name__ == "__main__":
    rows = load_results()

    plot_runtime_comparison(rows)
    plot_runtime_by_transfers(rows)
    plot_runtime_by_transfer_category(rows)
    plot_runtime_by_path_length(rows)
    plot_speedup_by_transfer_category(rows)