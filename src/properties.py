class AZUL_Property:
    def __init__(self, name: str):
        self.name = name
        self.values: dict[str: int] = {}
        self.counter = 0
                
    def addValue(self, name: str):
        self.values[name] = self.counter
        self.counter += 1

    def at(self, name: str):
        return self.values[name]
    
    def has(self, name: str):
        try:
            self.values[name]
            return True
        except Exception:
            return False
    
    def __repr__(self):
        return self.name