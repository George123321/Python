'''
def graph_smeg():
    n, m = [int(x) for x in input().split()]
    graph = [[] for i in range(n)]
    for i in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def bfs(graph, start = 0):
    fired = set()
    fired.add(start)
    Q = [start]
    derevo = []
    time = {start: 0}
    while Q:
        current = Q.pop(0)
        for neighbour in graph[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)
                derevo.append((current, neighbour))
                time[neighbour] = time[current] + 1
    return derevo, time

graph = graph_smeg()
d, t = bfs(graph)
print(d)
print(t)
'''
def lev(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)
print(lev(['h','o','u','s','e'], ['h','o','m','e']))