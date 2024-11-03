class PizzaStore:
    def orderPizza(self, type: str):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print('Pizza is ready !!')
        return pizza
    
    def createPizza(self, type):
        pass