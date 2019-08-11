graph = {}
graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def bfs(start):
    queue = [start]
    meet = {start}
    parent = {start: None}  # 添加一个parent记录前一个点的前一个点 构成了单源最短路算法
    while queue:
        tmp = queue.pop(0)
        for node in graph[tmp]:
            if node not in meet:
                parent[node] = tmp
                meet.add(node)
                queue.append(node)
        print(tmp)
    print(parent)


bfs('you')
