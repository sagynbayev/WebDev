def mini(a, b, c, d):
    if a <= b and a <= c and a <= d:
        return a
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    elif d <= a and d <= b and d <= c:
        return d
a, b, c, d = map(int, input().split())
print(mini(a, b, c, d))