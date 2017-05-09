n = int(input())
A = [int(x) for x in input().split()]
n = len(A)
B = []
A = sorted(A)
for i in range(n):
    if A[i]%2 != 0:
        B.append(A[i])
    else:
        A.append(A[i])
A = A[n:]
print(*B, *A[::-1])
