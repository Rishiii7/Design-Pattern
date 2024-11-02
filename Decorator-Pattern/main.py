from bevarage import Bevarage, BevarageSize
from concretebevarage import Espresso, DarkRoast, HouseBlend
from condimentsconcrete import Mocha, Whip, Soy, SteamedMilk


def main():
    print('#' * 20)
    bev1 = Espresso(BevarageSize.tall)
    print(bev1.getDescription())
    print('Order costs : ', bev1.cost())

    print('#' * 20)
    bev2 = DarkRoast(BevarageSize.grande)
    bev2 = Mocha(bev2)
    bev2 = Mocha(bev2)
    bev2 = Whip(bev2)
    print(bev2.getDescription())
    print('Order costs : ', bev2.cost())

    print('#' * 20)
    bev3 = HouseBlend(BevarageSize.venti)
    bev3 = Soy(bev3)
    bev3 = Mocha(bev3)
    bev3 = Whip(bev3)
    print(bev3.getDescription())
    print('Order Costs: ', bev3.cost())


main()