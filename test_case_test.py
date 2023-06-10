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
        self.assertEquals(expected= 'setUp testMethod tearDown ', actual= test.log)
    
    def testResult(self) :
        test = WasRun('testMethod')
        test.run(self.result)
        self.assertEquals(expected= '1 run, 0 failed', actual= self.result.summary())
    
    def testFailedResult(self) :
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        self.assertEquals(expected= '1 run, 1 failed\n(X) WasRun.testBrokenMethod Exception: ', actual= self.result.summary())

    def testFailedResultFormatting(self) :
        self.result.testStarted()
        self.result.testFailed(TestCaseTest('testBrokenMethod'), AssertionError('Error'))
        self.result.testStarted()
        self.result.testFailed(TestCaseTest('testFooBar'), ZeroDivisionError('ZeroDivisionError'))
        self.assertEquals('2 run, 2 failed\n(X) TestCaseTest.testBrokenMethod AssertionError: Error\n(X) TestCaseTest.testFooBar ZeroDivisionError: ZeroDivisionError', self.result.summary())

    def testSuite(self) :
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        suite.run(self.result)
        self.assertEquals(expected= '2 run, 1 failed\n(X) WasRun.testBrokenMethod Exception: ', actual= self.result.summary())

    def testTearDownCalledEventIfTestFailed(self) :
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        self.assertTrue(test.wasTearDownCalled)
        self.assertEquals(expected= '1 run, 1 failed\n(X) WasRun.testBrokenMethod Exception: ', actual= self.result.summary())
    
    def testCreateTestSuiteFromTestCaseClass(self) :
        suite = TestSuite.createFrom(WasRun)
        suite.run(self.result)
        self.assertEquals(expected= '2 run, 1 failed\n(X) WasRun.testBrokenMethod Exception: ', actual= self.result.summary())

    def testGetTestMethods(self) :
        actual = TestSuite.getTestMethodsIn(WasRun)
        expected = ['testMethod', 'testBrokenMethod']
        self.assertEquals(expected= set(expected), actual= set(actual))
    
    def testAssertTrue_WhenPassTrueValue(self) :
        assert(self.assertTrue(True) == None)
    
    def testAssertTrue_WhenPassFalseValue(self) :
        error_msg = ''
        try:
            self.assertTrue(False)
        except Exception as exception:
            error_msg = str(exception)
        assert('expected: True, but actual: False' == error_msg)
    
    def testAssertEquals_WhenActualEqualsExpected(self) :
        expected = 'test'
        actual = 'test'
        assert(self.assertEquals(expected, actual) == None)
    
    def testAssertEquals_WhenActualNotEqualsExpected(self) :
        error_msg = ''
        try:
            self.assertEquals(expected='test', actual='test_')
        except Exception as exception:
            error_msg = str(exception)
        assert("expected: 'test', but actual: 'test_'" == error_msg)

suite = TestSuite.createFrom(TestCaseTest)

result = TestResult()

suite.run(result)

print(result.summary())