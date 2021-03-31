n = int(input())
a = input().split()
cnt = 0
for i in range(1, n - 1):
    if (int(a[i - 1]) < int(a[i])) and (int(a[i + 1]) < int(a[i])):
        cnt += 1
print(cnt)