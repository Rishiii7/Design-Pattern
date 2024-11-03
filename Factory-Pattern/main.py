from pizzastore import PizzaStore
from pizzafactory import PizzaFactory

def main():
    pizza1 = PizzaStore(PizzaFactory())
    pizza1.orderPizza('Veggie')
    

main()
