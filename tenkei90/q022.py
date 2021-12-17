def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    return gcd(b, a % b)


a, b, c = map(int, input().split())
r = gcd(gcd(a, b), c)
print(a // r + b // r + c // r - 3)
