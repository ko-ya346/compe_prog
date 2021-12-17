class SegmentTreeL:
    def __init__(self, n):
        self.num = 1 << (n - 1).bit_length()
        self.data = [0] * (self.num * 2 - 1)
        self.lazy = [-1] * (self.num * 2 - 1)

    def eval(self, k):
        if self.lazy[k] == -1:
            return
        self.data[k] = self.lazy[k]
        if k < self.num - 1:
            self.lazy[2 * k + 1] = self.lazy[k]
            self.lazy[2 * k + 2] = self.lazy[k]
        self.lazy[k] = -1

    def update_ab(self, a, b, x):
        self.update_ab_sub(a, b, x, 0, 0, self.num)

    def update_ab_sub(self, a, b, x, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k] = x
            self.eval(k)
            return
        self.update_ab_sub(a, b, x, 2 * k + 1, l, (l + r) // 2)
        self.update_ab_sub(a, b, x, 2 * k + 2, (l + r) // 2, r)
        self.data[k] = max(self.data[2 * k + 1], self.data[2 * k + 2])

    def query(self, a, b):
        return self.query_sub(a, b, 0, 0, self.num)

    def query_sub(self, a, b, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.data[k]
        v1 = self.query_sub(a, b, 2 * k + 1, l, (l + r) // 2)
        v2 = self.query_sub(a, b, 2 * k + 2, (l + r) // 2, r)
        return max(v1, v2)


(W, N) = map(int, input().split())
LR_list = []
for _ in range(N):
    (l, r) = map(int, input().split())
    LR_list.append((l - 1, r))

sgt = SegmentTreeL(W)
for (l, r) in LR_list:
    m = sgt.query(l, r)
    print(m + 1)
    sgt.update_ab(l, r, m + 1)
