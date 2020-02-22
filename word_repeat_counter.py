sentence = [x.lower() for x in input().split()]
d = {}
for i in sentence:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for key, value in d.items():
    print(key + " " + str(value))
