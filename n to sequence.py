n = int(input())
out = []
i = 0
while len(out) < n:
    out += [i] * i
    i += 1
print(*out[:n])