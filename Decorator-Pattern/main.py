from bevarage import Bevarage
from concretebevarage import Espresso, DarkRoast, HouseBlend
from condimentsconcrete import Mocha, Whip, Soy, SteamedMilk


def main():
    print('#' * 20)
    bev1 = Espresso()
    print(bev1.getDescription())
    print('Order costs : ', bev1.cost())

    print('#' * 20)
    bev2 = DarkRoast()
    bev2 = Mocha(bev2)
    bev2 = Mocha(bev2)
    bev2 = Whip(bev2)
    print(bev2.getDescription())
    print('Order costs : ', bev2.cost())

    print('#' * 20)
    bev3 = HouseBlend()
    bev3 = Soy(bev3)
    bev3 = Mocha(bev3)
    bev3 = Whip(bev3)
    print(bev3.getDescription())
    print('Order Costs: ', bev3.cost())


main()