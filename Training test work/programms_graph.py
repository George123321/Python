def graph_smeg():
    n, m = [int(x) for x in input().split()]
    graph = [[] for i in range(n)]
    for i in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

#kvadrat
def kvadrat(graph):
    for vertex in range(len(graph)):
        for neighbour in graph[vertex]:
            for neighbour_neighbour in graph[neighbour]:
                if abs(neighbour_neighbour - vertex) == 2:
                    print((vertex, neighbour_neighbour))

#invert_graph
def invert(graph):
    ans = [[] for i in range(len(graph))]
    for vertex in range(len(graph)):
        for neighbour in graph[vertex]:
            ans[neighbour].append(vertex)
    return ans

#dopoln
def dopolnenie(graph):
    for vertex in range(len(graph)):
        for i in range(len(graph)):
            if i not in graph[vertex] and i != vertex:
                if (vertex, i) is None:
                    print('Граф полный')
                else:
                    print((vertex, i))


g = graph_smeg()
print(dopolnenie(g))