n = int(input())
a, b, c = map(int, input().split())

ans = float("inf")
for i in range(10000):
    for j in range(10000 - i):
        nokori = n - a * i - b * j
        if nokori >= 0 and nokori % c == 0:
            k = nokori // c
            if i + j + k <= 9999:
                ans = min(ans, i + j + k)

print(ans)
