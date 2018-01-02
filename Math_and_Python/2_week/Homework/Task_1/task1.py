import re
import numpy as np
s_file = open('sentences.txt')
n = 0
for line in s_file:
    n += 1
s_file = open('sentences.txt')
sentences = s_file.read().lower()
s_file.close()

sentences = re.findall(r'[a-z]+', sentences)

words = {}
for word in sentences:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

count = {}
i = 0
for word in words:
    count[word] = i
    i += 1

d = len(words)

frec = np.zeros((n, d))

s_file = open('sentences.txt')
s = s_file.read().lower()

i = 0
res = s.split('\n')
for line in res:
    res[i] = re.findall(r'[a-z]+', line)
    i += 1

i = 0
for line in res:
    for word in line:
        frec[i][count[word]] += 1
    i += 1
