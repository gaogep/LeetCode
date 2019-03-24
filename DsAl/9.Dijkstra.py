# 图
graph = {}
graph['start'] = {'a': 6, 'b': 2}
graph['a'] = {'fin': 1}
graph['b'] = {'a': 3, 'fin': 5}
graph['fin'] = {}

costs = {'a': 6, 'b': 2, 'fin': float('inf')}
parents = {'a': 'start', 'b': 'start', 'fin': None}
collected = []


def find_lowest_cost(costs):
    lowest_cost_node = None
    if costs:
        tmp = min(costs.items(), key=lambda x:x[1])[0]
        if tmp not in collected:
                lowest_cost_node = tmp
    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:   # 为什么其他点的开销要设置为无穷大的原因在这个不等式
                costs[n] = new_cost
                parents[n] = node
        collected.append(node)
        costs.pop(node)
        node = find_lowest_cost(costs)

dijkstra()
print(parents)