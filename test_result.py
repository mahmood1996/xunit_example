class TestFailure :
    def __init__(self, testCase, exception: Exception) -> None:
        self.testClassName = testCase.__class__.__name__
        self.testMethod = testCase.name
        self.exceptionName = exception.__class__.__name__
    
    def summary(self) -> str : 
        return f'(X) {self.testClassName}.{self.testMethod} {self.exceptionName}'

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