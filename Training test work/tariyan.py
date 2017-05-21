def graph_smeg():
    n, m = [int(x) for x in input().split()]
    graph = [[] for i in range(n)]
    for i in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1-1].append(v2-1)
        #graph[v2].append(v1)
    return graph
V = graph_smeg()
n = len(V)-1
Visited = [False] * (n + 1)
Ans = []

def DFS(start):
    Visited[start] = True
    for u in V[start]:
        if not Visited[u]:
            DFS(u)
    Ans.append(start)


for i in range(1, n + 1):
    if not Visited[i]:
        DFS(i)
Ans = Ans[::-1]
print(Ans)