import unittest




class demo(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(6, 9)

if __name__ == '__main__':
    unittest.main()