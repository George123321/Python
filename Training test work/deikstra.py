def input_W_slov():
    N, M = [int(x) for x in input().split()]
    G = {i: {} for i in range(N)}
    for i in range(M):
        v1, v2, w = [int(x) for x in input().split()]
        G[v1][v1] = 0
        G[v2][v2] = 0
        G[v1][v2] = w
        G[v2][v1] = w
    return G

def deikstra(G, start):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    used = set()
    while len(used) != len(G):
        min_d = float('+inf')
        for vertex in d:
            if d[vertex] < min_d and vertex not in used:
                min_d = d[vertex]
                current = vertex
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
        used.add(current)
    return d
graph = input_W_slov()
d = deikstra(graph, 1)
print(d)


