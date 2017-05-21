def Floyd(W, n, v1, v2): # W-весовая матрица, n - число ребер
    A = [[[10**9]*n for i in range(n)] for k in range(n)]
    for i in range(n):
        A[0][i][:] = W[i]
    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k]+A[k-1][k][j])
    return A[n][v1][v2]
