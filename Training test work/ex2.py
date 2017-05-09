n = int(input())
A = [1]
k = 1
while A[len(A)-1] <= n:
    A.append(k*A[k-1])
    k += 1
if A[len(A)-1] == n:
    print(*A[1:])
else:
    print(*A[1:len(A)-1])

