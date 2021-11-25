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
        input = """ABC"""
        output = """ARC"""
        self.assertIO(input, output)


def resolve():
    s = input()
    two = "BR"
    print(s[0] + two[s[1] == "B"] + s[2])


if __name__ == "__main__":
    unittest.main()
