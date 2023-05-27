from test_result import TestResult
from test_case import TestCase

class TestSuite:
    def __init__(self) :
        self.tests = []
    
    def add(self, test: TestCase):
        self.tests.append(test)
    
    def run(self, result: TestResult) :
        for test in self.tests :
            test.run(result)