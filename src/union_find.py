# https://atcoder.jp/contests/typical90/tasks/typical90_l
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])  # つなぎ直し
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def to_index(height, width, w):
    return height * w + width


h, w = map(int, input().split())
q = int(input())

uf = UnionFind(h * w)
color = [[False for _ in range(w)] for _ in range(h)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(q):
    t, *query = list(map(lambda x: int(x) - 1, input().split()))
    if t == 0:
        row, col = query

        # 該当箇所を赤く塗る
        color[row][col] = True

        # 上下左右を見て、赤い箇所があればunionする
        for nr, nc in move:
            nrow = row + nr
            ncol = col + nc
            if nrow >= h or nrow < 0 or ncol >= w or ncol < 0:
                continue
            p1 = to_index(nrow, ncol, w)
            p2 = to_index(row, col, w)

            if color[nrow][ncol]:
                uf.union(p1, p2)

    else:
        row1, col1, row2, col2 = query
        p1 = to_index(row1, col1, w)
        p2 = to_index(row2, col2, w)

        if color[row1][col1] and color[row2][col2] and uf.same(p1, p2):
            print("Yes")
        else:
            print("No")
