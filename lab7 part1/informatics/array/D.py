n = int(input())
a = input().split()
cnt = 0
for i in range(0, n):
    if int(a[i]) > int(a[0]):
        a[0] = a[i]
        cnt += 1
    else:
        a[0] = a[i]
print(cnt)  