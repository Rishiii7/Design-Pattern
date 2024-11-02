from enum import Enum

class BevarageSize(Enum):
    tall= .10
    grande= .15
    venti= .20


class Bevarage:
    def __init__(self, size: BevarageSize):
        self.description = 'Unkown Bevarage'
        self.size = size
    
    def getDescription(self):
        return self.description
    
    def cost(self):
        cost = 0
        if self.getSize() == BevarageSize.tall:
            cost += BevarageSize.tall.value
        elif self.getSize() == BevarageSize.grande:
            cost += BevarageSize.grande.value
        else:
            cost += BevarageSize.venti.value
        return cost

    def setDescription(self, description):
        self.description = description
    
    def getSize(self):
        return self.size

    def setSize(self, size: BevarageSize):
        self.size = size

