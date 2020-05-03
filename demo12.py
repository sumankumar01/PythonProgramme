import unittest
from HtmlTestRunner import HTMLTestRunner
import UnitTestPython
from UnitTestPython import unitExperiment

testList = [unitExperiment.CodeVlidation]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner=HTMLTestRunner(output='example_dir')
runner.run(newSuite)