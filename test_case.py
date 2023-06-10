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
    
    def assertTrue(self, actual: bool) :
        if not actual:
            raise AssertionError('expected: True, but actual: False')
    
    def assertEquals(self, expected, actual) :
        if (actual != expected):
            raise AssertionError(f"expected: '{expected}', but actual: '{actual}'")