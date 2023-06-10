from test_case import TestCase
from test_result import TestResult

class BrokenSetupTest(TestCase) :
    def setUp(self) :
        raise Exception()

    def testMethod(self) :
        pass

result = TestResult()

BrokenSetupTest('testMethod').run(result)

print(result.summary())