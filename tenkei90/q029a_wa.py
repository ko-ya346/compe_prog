class RMQ:
    """
    セグメント木
    指定範囲の最小値を親ノードが有する
    （最大値にしたい場合は、updateのwhile文のminをmaxに変更する）
    """

    def __init__(self, n, query=min):
        """
        arr: 配列
        """
        self.n = 1 << (n - 1).bit_length()

        self.query = query
        # セグメント木のノード数は2*n-1
        self.data = [0 for _ in range(self.n * 2 - 1)]
        # 遅延評価用の配列
        self.lazy = [-1 for _ in range(self.n * 2 - 1)]

    def eval(self, k):
        """
        配列のk番目を更新
        """
        if self.lazy[k] == -1:
            # 更新するものが無ければ終了
            return
        self.data[k] = self.lazy[k]
        if k < self.n - 1:
            # 葉でなければ子に伝搬
            self.lazy[k * 2 + 1] = self.lazy[k]
            self.lazy[k * 2 + 2] = self.lazy[k]
        self.lazy[k] = -1

    def update(self, i: int, x: int):
        """
        i番目の配列をxに置き換える
        """
        i += self.n - 1
        self.data[i] = x
        while i > 0:
            i = (i - 1) // 2
            child_l, child_r = (i * 2 + 1, i * 2 + 2)
            self.data[i] = self.query(self.data[child_l], self.data[child_r])

    def update_ab(self, a, b, x):
        """
        a, bの区間の値をxに更新する
        """
        self._update_ab_sub(a, b, x, 0, 0, self.n)

    def _update_ab_sub(self, a, b, x, k, l, r):
        self.eval(k)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k] = x
            self.eval(k)
            return
        self._update_ab_sub(a, b, x, k * 2 + 1, l, (l + r) // 2)  # 左の子
        self._update_ab_sub(a, b, x, k * 2 + 2, (l + r) // 2, r)  # 右の子
        self.data[k] = self.query(self.data[k * 2 + 1], self.data[k * 2 + 2])

    def get_query(self, a, b):
        """
        a, bの範囲内の最小（最大）を取得
        """

        def _query_sub(a, b, k, l, r):
            """
            k: 現在見ているノードの位置
            [l, r): dat[k]が表している区間
            """
            # 遅らせていた更新を実行
            self.eval(k)
            if r <= a or b <= l:
                return 0
            elif a <= l and r <= b:
                return self.data[k]
            else:
                vl = _query_sub(a, b, k * 2 + 1, l, (l + r) // 2)
                vr = _query_sub(a, b, k * 2 + 2, (l + r) // 2, r)
                return self.query(vl, vr)

        return _query_sub(a, b, 0, 0, self.n)


# a = [3, 5, 2, 11, 9, 6, 20, 8]
#
# rmq = RMQ(a)
#
# rmq.update_ab(0, 4, 1)
# print(vars(rmq))
# print(rmq.get_query(0, 5))

w, n = map(int, input().split())
renga = []
for _ in range(n):
    l, r = map(int, input().split())
    renga.append((l - 1, r))

rmq = RMQ(n, query=max)

for l, r in renga:
    print(vars(rmq))
    max_lr = rmq.get_query(l, r)
    print(max_lr + 1)
    rmq.update_ab(l, r, max_lr + 1)
