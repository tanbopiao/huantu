"""圜土（HUANTU）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_isolate_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.isolate(None, None)

    def test_check_escape_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.check_escape(None)


if __name__ == "__main__":
    unittest.main()
