def graph_smeg():
    n, m = [int(x) for x in input().split()]
    graph = [[] for i in range(n)]
    for i in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def dfs(graph, vertex=0, used = None):
    if used is None:
        used = set()
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(graph, neighbour, used)
graph = graph_smeg()
used = set()
num = 0
for vertex in range(len(graph)):
    if vertex not in used:
        dfs(graph, vertex, used)
        num += 1
print(num)
