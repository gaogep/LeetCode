graph = {}
graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque

def bfs(start):
    search_queue = deque()
    search_queue += graph[start]
    searchd = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searchd:
            print(person)
            search_queue += graph[person]
            searchd.append(person)

bfs('you')