from test_result import TestResult

class TestCase:
    def __init__(self, name: str) :
        self.name = name
    
    def setUp(self) :
        pass
    
    def tearDown(self) :
        pass

    def run(self) :
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except :
            result.testFailed()
        self.tearDown()
        return result