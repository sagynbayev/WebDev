a = int(input())
b = 0
i = 0
while(a != 0):
    c = a % 10
    b =  b + c * pow(2, i)
    a = a // 10
    i += 1
print(b)