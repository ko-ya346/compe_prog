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
        input = """
        """
        output = """
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
    pass


if __name__ == "__main__":
    unittest.main()
