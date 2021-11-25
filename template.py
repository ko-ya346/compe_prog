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
        print(stdout, stdin)
        sys.stdout, sys.stdin = StringIO(), StringIO(input)

        resolve()

        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test1(self):
        input = """
        4
4000 4400 5000 3200
3
3312
2992
4229

        """
        output = """
       112
208
171
 
        """
        self.assertIO(input, output)

    def test2(self):
        input = """
        """
        output = """
        
        """
        self.assertIO(input, output)

    def test3(self):
        input = """
        """
        output = """
        
        """
        self.assertIO(input, output)


def resolve():
    import bisect

    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = [int(input()) for _ in range(q)]

    for b in B:
        


if __name__ == "__main__":
    unittest.main()
