import numpy as np

w, n = map(int, input().split())
renga = []
num = set()
for _ in range(n):
    l, r = map(lambda x: int(x) - 1, input().split())
    renga.append((l, r))
    num.add(l)
    num.add(r)

d = dict(zip(sorted(list(num)), range(len(num))))

masu = np.zeros(len(d) + 1).astype(int)
for l, r in renga:
    li = d[l]
    ri = d[r]
    masu[li : ri + 1] = max(masu[li : ri + 1]) + 1
    print(max(masu[li : ri + 1]))
