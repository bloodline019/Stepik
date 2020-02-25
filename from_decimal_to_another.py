base = int(input("Введите разряд в который переводить число из 10-ой системы: "))
x = int(input("Введите число: "))
final = []
while x > 0:
    digit = x % base
    final.append(digit)
    x //= base
print(*reversed(final), " with base " + str(base), sep="")
