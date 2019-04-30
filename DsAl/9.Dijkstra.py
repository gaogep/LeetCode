import heapq  # 以优先队列的方式实现带权图的单源最短路算法
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def Dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = {s: 0}

    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        # 只有一个点从队列中被弹出来以后才会被认为是看到过了
        seen.add(vertex)
        for w in graph[vertex].keys():
            if w not in seen:
                # 如果从Vertex到W的花费比直接从起点到W的花费更小
                # 更新父节点表以及距离表
                dist + graph[vertex][w] < distance.get(w, math.inf):
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent, distance
