import matplotlib.pyplot as plt


def visualize_graph(nodes, posses, edges):
    fig, ax = plt.subplots(figsize=(10, 8))

    for u, v, w in edges:
        # Edge Line
        x_coords = [posses[u][0], posses[v][0]]
        y_coords = [posses[u][1], posses[v][1]]
        ax.plot(x_coords, y_coords, color='gray', linestyle='-', linewidth=1, zorder=1)

        # Edge Label
        mid_x = (posses[u][0] + posses[v][0]) / 2
        mid_y = (posses[u][1] + posses[v][1]) / 2
        ax.text(mid_x, mid_y, str(w), color='forestgreen', fontweight='bold',
                fontsize=10, ha='center', va='center', backgroundcolor='white', zorder=3)

    for node, (x, y) in posses.items():
        # Node Circle
        circle = plt.Circle((x, y), 0.3, color='royalblue', ec='black', lw=1.5, zorder=4)
        ax.add_patch(circle)

        # Node Label
        ax.text(x, y, node, color='white', fontweight='bold', ha='center', va='center', fontsize=12, zorder=5)

    ax.set_aspect('equal')
    ax.set_title("Digital Graph Reconstruction", fontsize=15, pad=20)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    all_x = [p[0] for p in posses.values()]
    all_y = [p[1] for p in posses.values()]
    plt.xlim(min(all_x) - 1, max(all_x) + 1)
    plt.ylim(min(all_y) - 1, max(all_y) + 1)

    plt.show()


if __name__ == "__main__":
    from final_project_part2_test import *
    visualize_graph(nodes, posses, edge_list)
