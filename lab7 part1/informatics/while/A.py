import math
a = int(input())
i = 1
while(i < (math.floor(math.sqrt(a)) + 1)):
    print(i**2)
    i += 1