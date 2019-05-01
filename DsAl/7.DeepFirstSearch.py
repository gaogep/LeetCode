graph = {}
graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anju', 'peg']
graph['alice'] = ['peg']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peg'] = []
graph['thom'] = []
graph['jonny'] = []
# ---------
searchd = []


def dfsr(start):
    for node in graph[start]:
        if node not in searchd:
            print(node)
            searchd.append(node)
            dfsr(node)


def dfsl(start):
    stack = []
    meet = set()
    stack.append(start)
    meet.add(start)
    while stack:
        tmp = stack.pop()
        for node in graph[tmp]:
            if node not in meet:
                stack.append(node)
                meet.add(node)
        print(tmp)


dfsl("you")
