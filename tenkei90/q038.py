import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)
ans = a // gcd * b
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)
