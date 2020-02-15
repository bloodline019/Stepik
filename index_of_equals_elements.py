lst = input().split()
x = input()
pos = 0
flag = False
for i in lst:
    if i == x:
        print(pos, end =" ")
        flag = True
    pos+=1
if not flag:
    print("Отсутствует")