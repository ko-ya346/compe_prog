n, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    if arr[i]:
        continue
    for j in range(i, n + 1, i):
        arr[j] += 1

print(sum([i >= k for i in arr]))
