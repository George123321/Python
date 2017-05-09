def read_graph_as_lists():
    N, M = [int(x) for x in input().split()]
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

c = 0
graph = read_graph_as_lists()
#print(graph)
for i in range(len(graph)):
    m = set(graph[i])
    if len(m) != len(graph)-1:
        c += 1
if c == 0:
    print('YES')
else:
    print('NO')