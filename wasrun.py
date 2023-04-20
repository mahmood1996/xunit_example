from test_case import TestCase

class WasRun(TestCase) :
    def __init__(self, name: str) :
        self.wasRun = None
        TestCase.__init__(self, name)
    
    def testMethod(self) :
        self.wasRun = 1
