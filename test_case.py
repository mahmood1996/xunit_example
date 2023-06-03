from test_result import TestResult

class TestCase:
    def __init__(self, name: str) :
        self.name = name
    
    def setUp(self) :
        pass
    
    def tearDown(self) :
        pass

    def run(self, result: TestResult) :
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception as exception:
            result.testFailed(self, exception)
        self.tearDown()