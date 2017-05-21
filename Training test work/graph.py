def deikstra(W):
    N = len(W)
    INF = 10 ** 9
    dist = [INF] * N
    dist[0] = 0
    used = set()
    ans = 0
    derevo = {}
    min_dist = INF
    vertex = 0
    for neighbour in W[vertex]:
        if not neighbour in used and dist[neighbour] < min_dist:
            min_dist = dist[neighbour]
            u = neighbour
    derevo[vertex] = u; derevo[u] = vertex
    used.add(u)
    for vertex in derevo:
        min_dist = INF
        for neighbour in W[vertex]:
            if not neighbour in used and dist[neighbour] < min_dist:
                min_dist = dist[neighbour]
                u = neighbour
        derevo[vertex] = u
        derevo[u] = vertex
    return derevo

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

G = input_W_slov()
print(G)
dist = deikstra(G)
print(dist)