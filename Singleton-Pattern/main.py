from chocolate import ChocolateBoiler

choco1 = ChocolateBoiler()
choco2 = ChocolateBoiler()

print(id(choco1)) 
print(id(choco2))  

choco1.fill()
print(choco2.isEmpty())
choco1.boil()
print(choco2.isBoiled())
print(choco1.isBoiled())  