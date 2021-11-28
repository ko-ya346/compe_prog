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
        input = """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6"""
        output = """63 261"""
        self.assertIO(input, output)

    def test2(self):
        input = """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7"""
        output = """72 172
23 172
23 183
63 89
115 89
95 261
63 261
138 183
135 261
138 261"""
        self.assertIO(input, output)

    def test3(self):
        input = """1
1 100
3
1 1
1 1
1 1"""
        output = """100 0
100 0
100 0"""
        self.assertIO(input, output)

    def test4(self):
        input = """20
2 90
1 67
2 9
2 17
2 85
2 43
2 11
1 32
2 16
1 19
2 65
1 14
1 51
2 94
1 4
1 55
2 90
1 89
1 35
2 81
20
3 17
5 5
11 11
8 10
3 13
2 6
3 7
3 5
12 18
4 8
3 16
6 8
3 20
1 12
1 6
5 16
3 10
17 19
4 4
7 15"""
        output = """175 430
0 85
0 65
51 16
116 246
67 154
0 165
0 111
213 184
32 156
175 340
32 54
299 511
132 336
67 244
175 314
51 181
124 90
0 17
120 186"""
        self.assertIO(input, output)


def resolve():
    import numpy as np

    n = int(input())
    c1 = [0]
    c2 = [0]

    for _ in range(n):
        c, p = map(int, input().split())
        if c == 1:
            c1.append(p)
            c2.append(0)
        else:
            c1.append(0)
            c2.append(p)

    c1c = np.cumsum(c1)
    c2c = np.cumsum(c2)

    q = int(input())

    for _ in range(q):
        l, r = map(int, input().split())
        print(c1c[r] - c1c[l - 1], c2c[r] - c2c[l - 1])


if __name__ == "__main__":
    unittest.main()
