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
    
    def assertRaises(self, expected_exception, function, *args) :
        def __format_exception(exception) :
            return f"{exception.__class__.__name__}('{str(exception)}')"

        def __areExceptionsEqual(exception, other) :
            return (exception.__class__ == other.__class__) and (str(exception) == str(other))
        
        result = None
        catched_exception = None

        try :
            result = function(args)
        except Exception as exc:
            catched_exception = exc
        
        if __areExceptionsEqual(catched_exception, expected_exception) :
            return

        error_msg = f"expected: raises {__format_exception(expected_exception)},"
        error_msg += f" but actual: raises {__format_exception(catched_exception)}" if catched_exception else f" but actual: returns {str(result)}"
        
        raise AssertionError(error_msg)