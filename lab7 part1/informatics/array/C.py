n = int(input())
a = input().split()
cnt = 0
for i in range(0, n):
    if int(a[i]) > 0:
        cnt += 1
print(cnt)