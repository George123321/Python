str = []
state = 0
for s in str:
    if state == 0:
        if s == 'a':
            state = 1
    elif state == 1:
        if s == 'b':
            state = 2
        elif s == 'a':
            state = 1
        else:
            state = 0
    elif state == 2:
        if s == 'c':
            state = 3
        elif s == 'a':
            state = 1
        else:
            state = 0
    elif state == 3:
        if s == 'd':
            state = 4
        elif s == 'a':
            state = 1
        else:
            state = 0
    elif state == 4:
        break