inf = open('textfile', 'r')
rec_line = inf.read().lower().split()
d = {}
rec_line.sort()
for i in rec_line:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
max_value = max(d.values())
for i in d:
    if d[i] == max_value:
        print(i + " " + str(max_value))
        break
