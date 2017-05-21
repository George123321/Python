A = [3, 6, 7, 32, 6, 87, 2, 65, 7]
'''
A = [6,3,7,32,6,87,2,65,7]
i = 0
for i in range(i+1, len(A)):
    j = i-1
    while A[j] >= A[i] and j >= 0:
        A[i], A[j] = A[j], A[i]
        i -= 1
        j -= 1
print(A)
'''
'''
A = [3, 6, 7, 32, 6, 87, 2, 65, 7]
for i in range(0, len(A)-1):
    m = i
    for j in range(i+1, len(A)):
        if A[j] < A[m]:
            m = j
    A[i], A[m] = A[m], A[i]
print(A)
'''
'''
A = [3, 6, 7, 32, 6, 87, 2, 65, 7]
for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j+1] < A[j]:
            A[j + 1], A[j] = A[j], A[j+1]
print(A)
'''
'''
i = 0
while i < len(A)-1:
    if A[i+1] < A[i]:
        A[i + 1], A[i] = A[i], A[i+1]
        i =0
    else:
        i+=1
print(A)
'''
'''
m = max(A) + 1
q = [0]*m
for x in A:
    q[x] += 1
for i in range(len(q)):
    for j in range(q[i]):
        print(i, end=' ')
'''
'''
def hoar(A):
    if len(A) <= 1:
        return A
    L = []
    M = []
    R = []
    b = A[0]
    for x in A:
        if x < b:
            L.append(x)
        if x == b:
            M.append(x)
        if x > b:
            R.append(x)
    return hoar(L) + M + hoar(R)
print(hoar(A))
'''
'''
def merge(L, R):
    C = [None]*(len(L)+len(R))
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            C[k] = L[i]
            k += 1
            i += 1
        else:
            C[k] = R[j]
            k += 1
            j += 1
    C[k:] = L[i:] + R[j:]
    return C

def merge_sort(A):
    if len(A) <= 1:
        return A
    L = merge_sort(A[:len(A)//2])
    R = merge_sort(A[len(A)//2:])
    return merge(L, R)

print(merge_sort(A))
'''
'''
def evklid(a, b):
    if a < b:
        c = a
        a = b
        b = c
    assert a >= b
    if a == 0 and b == 0:
        return max(a, b)
    return evklid(a%b, b)
'''
'''
def evklid(a, b):
    if a < b:
        c = a
        a = b
        b = c
    while a != 0 and b != 0:
        a = a%b
        if a < b:
            c = a
            a = b
            b = c
    return max(a, b)
print(evklid(175, 90))
'''
'''
def fasr_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return a**2**(n//2)
    else:
        return a*fasr_pow(a, n-1)
print(fasr_pow(2, 5))
'''
'''
def hanoi(n, i=1, j=2):
    if n == 1:
        print('Переложить блин 1 с', i, 'на', j)
    else:
        k = 6 - i - j
        hanoi(n-1, i, k)
        print('Переложить блин', n, 'с', i, 'на', j)
        hanoi(n-1, k, j)
hanoi(3)
'''
def deikstra(W):
    N = len(W)
    INF = 10 ** 9
    dist = [INF] * N
    dist[0] = 0
    used = set()
    ans = 0
    for i in range(N):
        min_dist = INF
        for j in range(N):
            if j not in used and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        ans += min_dist
        used.add(u)
        for v in range(N):
            dist[v] = min(dist[v], W[u][v])
    return dist

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
