def prefix(s):
    n = len(s)
    pi = [0]*n
    for i in range(1, len(s)):
        temp = pi[i-1]
        while temp > 0 and s[i] != s[temp]:
            temp -= 1
        if s[i] == s[temp]:
            pi[i] = pi[i-1] + 1
        else:
            pi[i] = 0
    return pi
print(prefix(['a','b','a','c','a','b','a']))
