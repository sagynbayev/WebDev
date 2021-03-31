a = int(input())
b = int(input())
for x in [i * i for i in range(b + 1) 
    if i * i>= a and i * i <= b]:
        print(x)