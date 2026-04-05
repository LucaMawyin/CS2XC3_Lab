from final_project_part1 import * 
import matplotlib.pyplot as plt 
import random 
import time 


sizes = [i for i in range(0,50)] 
trials = 1

dijkstra_times = [] 
bellman_times = [] 
mystery_times = []

for n in sizes:
    d_time_total = 0 
    b_time_total = 0 
    m_time_total = 0
    for _ in range(trials):
        G = create_random_complete_graph(n,100)

        start = time.time()
        for s in range(n):
            dijkstra(G,s)
        end = time.time()
        d_time_total += (end - start)

        start = time.time()
        for s in range(n):
            bellman_ford(G,s)
        end = time.time()
        b_time_total += (end - start)

        start = time.time()
        mystery(G)
        end = time.time()
        m_time_total += (end - start)

    dijkstra_times.append(d_time_total / trials) 
    bellman_times.append(b_time_total / trials) 
    mystery_times.append(m_time_total / trials)

plt.loglog(sizes, dijkstra_times, label='Dijkstra (All-Pairs)', marker='o')
plt.loglog(sizes, bellman_times, label='Bellman-Ford (All-Pairs)', marker='o')
plt.loglog(sizes, mystery_times, label='Mystery', marker='o')

plt.xlabel('log(Number of Nodes)')
plt.ylabel('log(Runtime (seconds))')
plt.title('Log-Log Runtime Comparison (Dense Graph)')
plt.legend()
plt.xticks([10, 20, 30, 40, 50])
plt.show()