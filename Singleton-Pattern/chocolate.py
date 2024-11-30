class ChocolateBoiler:
    __instane = None

    def __new__(cls):
        if cls.__instane is None:
            cls.__instane = super().__new__(cls)
        return cls.__instane

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.empty = True
            self.boiled = False
            self.initialized = True
    
    def isEmpty(self):
        return self.empty

    def isBoiled(self):
        return self.boiled

    def fill(self):
        if (self.isEmpty()):
            self.empty = False
            self.boiled = False
        else:
            print(f'Cannot fill the mixture, it is not empty')
    
    def drain(self):
        if( not self.isEmpty() and self.isBoiled()):
            self.empty = True
        else:
            print(f'Cannot Drain the mixture')

    def boil(self):
        if( not self.isEmpty() and not self.isBoiled()):
            self.boiled = True
        else:
            print(f'cannot boil')
    
    
