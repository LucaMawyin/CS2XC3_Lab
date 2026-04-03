
if __name__ == "__main__":
    import final_project_part2_test as p2t
    import final_project_part4 as p4

    for x in p2t.nodes:
        for y in p2t.nodes:
            dwg = p4.WeightedGraph()
            dwg.adj = p2t.g.adj
            dwg.weights = p2t.g.weights

            hg = p4.HeuristicGraph(p2t.calc_h(y))
            hg.adj = p2t.g.adj
            hg.weights = p2t.g.weights

            res1 = p4.Dijkstra.calc_sp(dwg, x, y)
            res2 = p4.Bellman_Ford.calc_sp(dwg, x, y)
            res3 = p4.A_Star.calc_sp(hg, x, y)

            assert res1 == res2, f"failed on {x} -> {y}"
            assert res2 == res3, f"failed on {x} -> {y}"

    print("done")
