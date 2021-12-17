n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    k -= abs(a[i] - b[i])

if k >= 0 and k % 2 == 0:
    print("Yes")
else:
    print("No")
