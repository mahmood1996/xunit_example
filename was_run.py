from test_case import TestCase

class WasRun(TestCase) :
    def __init__(self, name: str) :
        TestCase.__init__(self, name)
    
    def setUp(self) :
        self.log = 'setUp '
        self.wasTearDownCalled = False

    def testMethod(self) :
        self.log = self.log + 'testMethod '

    def testBrokenMethod(self) :
        raise Exception()

    def tearDown(self) :
        self.log = self.log + 'tearDown '
        self.wasTearDownCalled = True
