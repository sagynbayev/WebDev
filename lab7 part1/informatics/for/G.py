a = int(input())
x = 2
for i in range(a, 1, -1):
    if(a % i == 0):
        x = i
print(x)