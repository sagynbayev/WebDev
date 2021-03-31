n = int(input())
a = input().split()
for i in range(0, n):
    if int(a[i]) % 2 == 0:
        print(a[i], end=" ")