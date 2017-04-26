__author__ = 'student'
import re

def read_rules():
    f = open('rules.txt')
    rules = []
    for line in f:
        rules.extend(re.findall("^(.)q(\d+)->(.)(q(\d+)(.)|STOP)$", line))
    return rules

def read_lenta():
    lenta = ['B']
    f = open('line.txt').read()
    for x in f:
        lenta.append(x)
    lenta.extend('B')
    return lenta

def karetka(rules, lenta, k, state): # пишем для катой клетки
    k = int(k)
    for line in rules:
        if lenta[k] == line[0] and state == int(line[1]):
            lenta[k] = line[2]
            state = int(line[4])
            if line[5] == 'R':
                k += 1
                return lenta, k, state
            if line[5] == 'L':
                k -= 1
                return lenta, k, state
            if line[3] == 'STOP':
                return lenta, k, 'end'


def magic(rules, lenta, k, state):
    x = True
    state = 1
    while x == True:
        lenta, k, state = karetka(rules, lenta, k, state)
        if state == 'end':
            x = False
    return lenta

rules = read_rules()
lenta = read_lenta()
print(magic(rules, lenta, 1, 1))
