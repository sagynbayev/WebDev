a = int(input())
res = 0
while a > 0:
    x = a % 10
    a = a // 10
    res = res * 10
    res = res + x
print(res)