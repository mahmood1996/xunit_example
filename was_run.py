from test_case import TestCase

class WasRun(TestCase) :
    def __init__(self, name: str) :
        TestCase.__init__(self, name)
    
    def setUp(self) :
        self.log = 'setUp '

    def testMethod(self) :
        self.log = self.log + 'testMethod '
