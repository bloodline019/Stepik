inf = open('textfile.txt', 'r')
ouf = open('textoutput.txt', 'w')
rec_lines = inf.read().split()
ready_lines = []
rating_list = [0 for i in range(3)]
for i in rec_lines:
    ready_lines.append(i.split(";")[1:])
for i in ready_lines:
    rating = 0
    for j in range(len(i)):
        rating += int(i[j])
        rating_list[j] += int(i[j])
    print(rating / 3, file=ouf, end="\n")
for i in rating_list:
    print(i / len(ready_lines), file=ouf, end=" ")
