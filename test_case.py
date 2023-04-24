class TestCase:
    def __init__(self, name: str) :
        self.name = name
    
    def setUp(self) :
        pass
    
    def run(self) :
        self.setUp()
        method = getattr(self, self.name)
        method()