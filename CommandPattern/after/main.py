from chef import Chef
from waiter import Waiter
from pizza_order import PizzaOrder
from burger_order import BurgerOrder

chef=Chef()
waiter=Waiter()

waiter.take_order(PizzaOrder(chef))
waiter.take_order(BurgerOrder(chef))