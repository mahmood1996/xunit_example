from test_case import TestCase
from was_run import WasRun

class TestCaseTest(TestCase) :
    def setUp(self) :
        self.test = WasRun('testMethod')

    def testSetUp(self) :
        self.test.run()
        assert(self.test.wasSetUp)
    
    def testRunning(self) :
        self.test.run()
        assert(self.test.wasRun)
    
    
TestCaseTest('testRunning').run()
TestCaseTest('testSetUp').run()