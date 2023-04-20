from test_case import TestCase
from was_run import WasRun

class TestCaseTest(TestCase) :
    def testRunning(self) :
        test = WasRun('testMethod')
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest('testRunning').run()