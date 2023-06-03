from re import search
from test_case import TestCase
from was_run import WasRun
from test_result import TestResult
from test_suite import TestSuite

class TestCaseTest(TestCase) :

    def setUp(self) :
        self.result = TestResult()

    def testTemplateMethod(self) :
        test = WasRun('testMethod')
        test.run(self.result)
        assert('setUp testMethod tearDown ' == test.log)
    
    def testResult(self) :
        test = WasRun('testMethod')
        test.run(self.result)
        assert('1 run, 0 failed' == self.result.summary())
    
    def testFailedResult(self) :
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        assert('1 run, 1 failed\n(X) WasRun.testBrokenMethod Exception' == self.result.summary())

    def testFailedResultFormatting(self) :
        self.result.testStarted()
        self.result.testFailed(TestCaseTest('testBrokenMethod'), AssertionError())
        self.result.testStarted()
        self.result.testFailed(TestCaseTest('testFooBar'), ZeroDivisionError())
        assert('2 run, 2 failed\n(X) TestCaseTest.testBrokenMethod AssertionError\n(X) TestCaseTest.testFooBar ZeroDivisionError' == self.result.summary())

    def testSuite(self) :
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        suite.run(self.result)
        assert('2 run, 1 failed\n(X) WasRun.testBrokenMethod Exception' == self.result.summary())

    def testTearDownCalledEventIfTestFailed(self) :
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        assert(test.wasTearDownCalled)
        assert('1 run, 1 failed\n(X) WasRun.testBrokenMethod Exception' == self.result.summary())
    
    def testCreateTestSuiteFromTestCaseClass(self) :
        suite = TestSuite.createFrom(WasRun)
        suite.run(self.result)
        assert('2 run, 1 failed\n(X) WasRun.testBrokenMethod Exception' == self.result.summary())

    def testGetTestMethods(self) :
        actual = TestSuite.getTestMethodsIn(WasRun)
        expected = ['testMethod', 'testBrokenMethod']
        assert(set(actual) == set(expected))

suite = TestSuite.createFrom(TestCaseTest)

result = TestResult()

suite.run(result)

print(result.summary())