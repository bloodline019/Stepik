def modify_list(l):
    prom = list(filter(lambda x: x % 2 == 0, l))
    for i in range(len(l)):
        prom[i] //= 2
    for i in range(len(l)-1,-1,-1):
        del l[i]
        for i in prom:
            l.append(i)