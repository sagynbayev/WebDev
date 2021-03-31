def xor(a, b):
    res = a ^ b
    return res
a, b = map(int, input().split())
print(xor(a, b))