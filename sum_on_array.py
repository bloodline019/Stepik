array = []
while True:
    inp = input().split()
    if inp[0] == "end":
        break
    inp = list(map(int, inp))
    array += [inp]
for i in range(len(array)):
    if i > 0:
        print()
    for j in range(len(array[i])):
        if len(array) == 1 and len(array[i]) == 1:
            value = array[i][j]*4
            print(value)
            break
        elif i == 0 and j == len(array[i]) - 1 and len(array) == 1:
            value = array[-1][j] + array[-1][j] + array[i][j - 1] + array[i][0]
        elif i == 0 and j == len(array[i]) - 1:
            value = array[-1][j] + array[i + 1][j] + array[i][j - 1] + array[i][0]
        elif i != 0 and i != len(array) - 1 and j == len(array[i]) - 1 :
            value = array[i - 1][j] + array[i + 1][j] + array[i][j - 1] + array[i][0]
        elif i == len(array) - 1 and j == len(array[i]) - 1:
            value = array[i-1][j] + array[0][j] + array[i][j - 1] + array[i][0]
        elif i == len(array) - 1 and j != len(array[i]) - 1:
            value = array[i - 1][j] + array[0][j] + array[i][j - 1] + array[i][j + 1]
        elif i == len(array) - 1 and j == 0:
            value = array[i - 1][j] + array[0][j] + array[i][-1] + array[i][j + 1]
        else:
            value = array[i-1][j] + array[i+1][j] + array[i][j-1] + array[i][j+1]
        print(value, end=" ")
        j += 1
    i += 1


c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()

















