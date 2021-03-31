a = int(input())
sum = 0
for i in range(a):
    sum += a % 10
    a //= 10
print(sum)