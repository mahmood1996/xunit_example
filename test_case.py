class TestCase:
    def __init__(self, name: str) :
        self.name = name
    
    def run(self) :
        method = getattr(self, self.name)
        method()