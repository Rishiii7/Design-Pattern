from pizzafactory import PizzaFactory

class PizzaStore:
    def __init__(self, factory: PizzaFactory):
        self.factory = factory

    def orderPizza(self, type: str):
        pizza = self.factory.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print('Pizza is ready !!')
        return pizza