from test_case import TestCase

class WasRun(TestCase) :
    def __init__(self, name: str) :
        TestCase.__init__(self, name)
    
    def setUp(self) :
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self) :
        self.wasRun = 1
