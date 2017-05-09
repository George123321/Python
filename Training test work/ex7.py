def read_graph_as_lists():
    N, M = [int(x) for x in input().split()]
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

def dfs(vertex, graph, Color = 123, IsBipartite = None, used = None): # Depth-first search
    if Color == 123:
        Color = [1]+[0] * (len(graph))
    if used is None:
        used = set()
    if IsBipartite is None:
        IsBipartite = []
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour in used:
            if Color[vertex] == Color[neighbour]:
                IsBipartite.append(False)
        if neighbour not in used:
            if Color[vertex] == 1:
                Color[neighbour] = 2
            if Color[vertex] == 2:
                Color[neighbour] = 1
            dfs(neighbour, graph, Color, IsBipartite, used)
    return IsBipartite, Color

def Is_Bipartite(graph):
    A, Color = dfs(0, graph)
    if A == []:
        return True, Color
    else:
        return False, Color

graph = read_graph_as_lists()
flag, color = Is_Bipartite(graph)
if flag:
    print('YES')
    for i in range(len(color)):
        if color[i] == 1:
            print(i+1, end=' ')
else:
    print('NO')
