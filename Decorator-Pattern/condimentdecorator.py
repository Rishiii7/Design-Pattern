from bevarage import Bevarage

class CondimentsDecorator(Bevarage):
    def __init__(self, bev: Bevarage):
        self.bev = bev
        
    def getDescription(self):
        pass
