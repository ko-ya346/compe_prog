import numpy as np

n = int(input())
arr = np.zeros((1001, 1001))
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    # 2次元いもす法
    arr[ly, lx] += 1
    arr[ry, lx] -= 1
    arr[ly, rx] -= 1
    arr[ry, rx] += 1

arr = np.cumsum(np.cumsum(arr, axis=1), axis=0).astype(int)
k, cnt = np.unique(arr, return_counts=True)
d = dict(zip(range(0, n + 1), [0] * (n + 1)))
for i in range(len(k)):
   d[k[i]] = cnt[i]

for v in list(d.values())[1:]:
   print(v)

