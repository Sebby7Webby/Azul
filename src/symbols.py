from properties import *
from errors import *

class AZUL_Symbol:
    symbols: dict[str: any] = {}

    def __init__(self, symbol: str, properties: dict[AZUL_Property: int]):
        self.symbol = symbol
        self.properties: dict[AZUL_Property: int] = properties
        try:
            AZUL_Symbol.symbols[self.symbol]
            raise ERR_AZUL_SymbolDefinedTwice(f"Symbol character(s) of '{self.symbol}' has already been used")
        except KeyError:
            AZUL_Symbol.symbols[self.symbol] = self
    
    def createChanged(self, toChange: str):
        d: dict[AZUL_Property: int] = {}

        for property in self.properties.items():
            if property[0].has(toChange):
                d[property[0]] = property[0].at(toChange)
            else:
                d[property[0]] = property[1]
        return d
    
    def __repr__(self):
        return self.symbol


class AZUL_SymbolTable:
    def __init__(self):
        self.table: list = []

    def makeTable(self, properties: list[AZUL_Property]):
        def traverse(l):
            if not l:
                yield l
            else:
                for sublist in l:
                    yield from traverse(sublist)

        for property in properties:
            for point in traverse(self.table):
                if property == properties[len(properties)-1]:
                    point.extend(['' for _ in range(len(property.values))])
                else:
                    point.extend([[] for _ in range(len(property.values))])
    
        
    def findSymbol(self, symbol: AZUL_Symbol):
        values = list(symbol.properties.values())
        curr = self.table
        for i, value in enumerate(values):
            if (i == len(values)-1):
                break
            curr = curr[value]
        
        return curr[values[len(values)-1]]
    
    def setSymbol(self, symbol: AZUL_Symbol):
        values = list(symbol.properties.values())
        curr = self.table
        for i, value in enumerate(values):
            if (i == len(values)-1):
                break
            curr = curr[value]
        
        curr[values[len(values)-1]] = symbol
    
    def __repr__(self):
        pass
        


manner = AZUL_Property('manner')

manner.addValue('plosive')
manner.addValue('fricative')
manner.addValue('liquid')
manner.addValue('nasal')

place = AZUL_Property('place')

place.addValue('alveolar')
place.addValue('palatal')
place.addValue('velar')
place.addValue('labial')
place.addValue('glottal')

voicing = AZUL_Property('voicing')

voicing.addValue('devoiced')
voicing.addValue('voiced')

n = AZUL_Symbol('n', {manner: manner.at('nasal'), place: place.at('alveolar'), voicing: voicing.at('voiced')})
m = AZUL_Symbol('m', {manner: manner.at('nasal'), place: place.at('labial'), voicing: voicing.at('voiced')})


table = AZUL_SymbolTable()
table.makeTable([manner, place, voicing])
table.setSymbol(n)
table.setSymbol(m)

print(m.createChanged('devoiced'))