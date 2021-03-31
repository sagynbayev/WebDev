import math
a = int(input())
cnt = 0
for i in range(1, math.floor(math.sqrt(a)) + 1):
    if a % i == 0:
        if(a // i == i):
            cnt += 1
        else:
            cnt += 2
print(cnt)