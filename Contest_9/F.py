A = [int(x) for x in input().split()]
A = sorted(A)
used = set()
c = 0
for elem in A:
    if elem not in used:
        for i in range(len(A)):
            if A[i] == elem:
                c += 1
    else:
        continue
    used.add(elem)
    print(elem, c)
    c = 0
#Нафиг дерево для сортировки!