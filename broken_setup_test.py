from test_case import TestCase

class BrokenSetupTest(TestCase) :
    def setUp(self) :
        raise Exception()

    def testMethod(self) :
        pass

print(BrokenSetupTest('testMethod').run().summary())