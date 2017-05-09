n = int(input())
A = [int(x) for x in input().split()]
coins = 0
start = 0
ans = 0
for i in range(n):
    if A[i] == 5:
        coins -= 1
    else:
        coins += A[i]//5 - 1
if coins <= 0:
    coins = 0
print(coins) #FIXME
