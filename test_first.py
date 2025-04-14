import unittest
import first

class Testing(unittest.TestCase):
    def test_one(self):
        ok = 6
        result = first.plus(2, 4)
        self.assertEqual(ok, result)

if __name__ == '__main__':
    unittest.main()
