import pytest
import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner

class CodeVlidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Executed Before the all the method executed in class')

    @classmethod
    def tearDownClass(cls):
        print('xecuted after the all the method executed in class')


    def setUp(self):
        print("Setup the environment")
    def tearDown(self):
        print("cleaning the environment")

    def testcase1(self):

        print("running the test case1")
        self.assertEqual(2, 2)

    def testcase2(self):
        print("running the test case2")
        self.assertEqual(2, 3)

# def suite():
#     suite = unittest.TestSuite()
#         ##   suite.addTest (CodeVlidation("testcase1"))
#         ##   suite.addTest (CodeVlidation("testcase2"))
#     suite.addTest(unittest.makeSuite(CodeVlidation))
#     return suite
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run (test_suite)

# if __name__ == '__main__':
#
#     testList = [CodeVlidation]
#     testLoad = unittest.TestLoader()
#
#     TestList = []
#     for testCase in testList:
#         testSuite = testLoad.loadTestsFromTestCase(testCase)
#         TestList.append(testSuite)
#
#     newSuite = unittest.TestSuite(TestList)
#     runner = unittest.TextTestRunner()
#     runner=HTMLTestRunner(output='example_dir')
#     runner.run(newSuite)