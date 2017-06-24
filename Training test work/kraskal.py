#граф как кортеж ребро - вес, n - количество вершин
def input_graph():
    n, m = [int(x) for x in input().split()]
    graph = []
    for i in range(m):
        w, v1, v2 = [int(x) for x in input().split()]
        graph.append([w, v1, v2])
    return graph, n

def kraskal(graph, n):
    comp = [i for i in range(n)]
    derevo = []
    graph.sort()
    for weigh, v1, v2 in graph:
        if comp[v1] != comp[v2]:
            derevo.append((v1, v2))
            a = comp[v1]
            b = comp[v2]
            for i in range(n):
                if comp[i] == b:
                    comp[i] = a
    return derevo
g, n = input_graph()
print(kraskal(g, n))
