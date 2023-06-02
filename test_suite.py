from test_result import TestResult
from test_case import TestCase

class TestSuite:
    def createFrom(testCaseClass: type[TestCase]) -> 'TestSuite' :
        suite = TestSuite()

        test_methods = TestSuite.getTestMethodsIn(testCaseClass)

        for test_method in test_methods:
            TestSuite.__addTestCaseToSuite(testCaseClass(test_method), suite)
    
        return suite
    
    def __addTestCaseToSuite(testCase: TestCase, suite: 'TestSuite') :
        suite.add(testCase)

    def getTestMethodsIn(testCaseClass: type[TestCase]) -> list[str]:
        attributes = dir(testCaseClass)
        test_methods_names = filter(lambda e: str(e).startswith('test'), attributes)
        return list(test_methods_names)

    def __init__(self) :
        self.tests = []
    
    def add(self, test: TestCase):
        self.tests.append(test)
    
    def run(self, result: TestResult) :
        for test in self.tests :
            test.run(result)