"""圜土（HUANTU）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from huantu import Huantu


class TestHuantu(unittest.TestCase):
    def setUp(self):
        self.op = Huantu()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "huantu")
        self.assertEqual(d["code"], "HUANTU")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_isolate(self):
        ok = self.op.isolate(lambda a, b: a + b, (1, 2))
        self.assertTrue(ok["ok"])
        self.assertEqual(ok["result"], 3)
        bad = self.op.isolate(lambda: 1 / 0, ())
        self.assertFalse(bad["ok"])

    def test_check_escape(self):
        self.assertTrue(self.op.check_escape({"type": "network"})["escaped"])
        self.assertFalse(self.op.check_escape({"type": "compute"})["escaped"])


if __name__ == "__main__":
    unittest.main()
