n = int(input())
a = input().split()
isTrue = False
for i in range(0, n - 1):
    if (int(a[i]) >= 0 and int(a[i + 1]) >= 0) or (int(a[i]) < 0 and int(a[i + 1]) < 0):
        isTrue = True
        break
if isTrue:
    print("YES")
else:
    print("NO")