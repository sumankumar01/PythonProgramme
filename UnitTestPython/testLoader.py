import unittest

testList = [testcase1(), testcase1()]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)