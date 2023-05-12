from test_case import TestCase
from was_run import WasRun
from broken_setup_test import BrokenSetupTest
from test_result import TestResult

class TestCaseTest(TestCase) :
    def testTemplateMethod(self) :
        test = WasRun('testMethod')
        test.run()
        assert('setUp testMethod tearDown ' == test.log)
    
    def testResult(self) :
        test = WasRun('testMethod')
        result = test.run()
        assert('1 run, 0 failed' == result.summary())
    
    def testFailedResult(self) :
        test = WasRun('testBrokenMethod')
        result = test.run()
        assert('1 run, 1 failed' == result.summary())

    def testFailedResultFormatting(self) :
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert('1 run, 1 failed' == result.summary())

TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()
TestCaseTest('testFailedResultFormatting').run()
TestCaseTest('testFailedResult').run()