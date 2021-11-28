"""
io.StringIO: 標準モジュール
「ファイルオブジェクトのように見えるオブジェクト」を作れる
"""

import sys
import unittest
from io import StringIO


class TestCase(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)

        resolve()

        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test1(self):
        input = """10
attcordeer"""
        output = """4"""
        self.assertIO(input, output)

    def test2(self):
        input = """41
btwogablwetwoiehocghiewobadegwhoihegnldir"""
        output = """2"""
        self.assertIO(input, output)

    def test3(self):
        input = """140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr"""
        output = """279999993"""
        self.assertIO(input, output)


def resolve():
    import numpy as np

    n = int(input())
    S = input()
    t = "atcoder"
    dp = np.zeros((n + 1, len(t) + 1), dtype=int)
    dp[0, 0] = 1
    mod = 10 ** 9 + 7

    for i, s in enumerate(S):
        # i+1文字目を選ばない
        dp[i + 1, :] += dp[i, :]
        dp[i + 1, :] %= mod
        if s not in t:
            continue

        # i+1文字目を選ぶ
        idx = t.index(s)
        dp[i + 1, idx + 1] += dp[i, idx]
        dp[i + 1, idx + 1] %= mod

    print(dp[-1, -1])


if __name__ == "__main__":
    unittest.main()
