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
        assert('1 run, 1 failed' == self.result.summary())

    def testFailedResultFormatting(self) :
        self.result.testStarted()
        self.result.testFailed()
        assert('1 run, 1 failed' == self.result.summary())

    def testSuite(self) :
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        suite.run(self.result)
        assert('2 run, 1 failed' == self.result.summary())

    def testTearDownCalledEventIfTestFailed(self) :
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        assert(test.wasTearDownCalled)
        assert('1 run, 1 failed' == self.result.summary())
    
    def testCreateTestSuiteFromTestCaseClass(self) :
        suite = createTestSuiteFrom(WasRun)
        suite.run(self.result)
        assert('2 run, 1 failed' == self.result.summary())

    def testGetNamesOfTestMethods(self) :
        actual = getNamesOfTestMethodsIn(WasRun)
        expected = ['testMethod', 'testBrokenMethod']
        assert(set(actual) == set(expected))

def createTestSuiteFrom(testCaseClass: type[TestCase]) -> TestSuite : 
    suite = TestSuite()

    tests_names = getNamesOfTestMethodsIn(testCaseClass)

    for test_method_name in tests_names:
        test = testCaseClass(test_method_name)
        suite.add(test)
    
    return suite

def getNamesOfTestMethodsIn(testCaseClass: type[TestCase]) -> list[str]:
    attributes = dir(testCaseClass)
    test_methods_names = filter(lambda e: str(e).startswith('test'), attributes)
    return list(test_methods_names)

suite = createTestSuiteFrom(TestCaseTest)

result = TestResult()

suite.run(result)

print(result.summary())