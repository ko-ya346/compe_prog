import sys

sys.setrecursionlimit(10 ** 6)


def dfs(pos, cur):
    col[pos] = cur
    for i in tree[pos]:
        if col[i] == -1:
            dfs(i, 1 - cur)


n = int(input())

tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    tree[a].append(b)
    tree[b].append(a)

col = [-1 for _ in range(n)]
dfs(0, 0)

g0 = []
g1 = []
for i, c in enumerate(col):
    if c:
        g0.append(i + 1)
    else:
        g1.append(i + 1)

if len(g0) >= n // 2:
    print(*g0[: n // 2])
else:
    print(*g1[: n // 2])
