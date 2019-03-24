graph = {}
graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anju', 'peg']
graph['alice'] = ['peg']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peg'] = []
graph['thom'] = []
graph['jonny'] = []

searchd = []
def dfs(start):
    for node in graph[start]:
        if node not in searchd:
            print(node)
            searchd.append(node)
            dfs(node)

dfs('you')
