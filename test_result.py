class TestFailure :
    def __init__(self, testCase, exception: Exception) -> None:
        self.testClassName = testCase.__class__.__name__
        self.testMethod = testCase.name
        self.exception = exception
    
    def summary(self) -> str : 
        return f'(X) {self.testClassName}.{self.testMethod} {self.__format_exception()}'
    
    def __format_exception(self) :
        return f'{self.exception.__class__.__name__}: {self.exception}'

class TestResult :
    def __init__(self) :
        self.runCount = 0
        self.failures = []
    
    def testStarted(self) :
        self.runCount = self.runCount + 1
    
    def testFailed(self, testCase, exception: Exception) :
        self.failures.append(TestFailure(testCase, exception))

    def summary(self) :
        summary = '%d run, %d failed' % (self.runCount, len(self.failures))
        for failure in self.failures :
            summary += f'\n{failure.summary()}'
        return summary