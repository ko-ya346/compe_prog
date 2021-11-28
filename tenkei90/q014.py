n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    ans += abs(a[i] - b[i])

print(ans)
