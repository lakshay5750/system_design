from discount_service import DiscountService
from diwali import Diwali
from holi import Holi

holi=Holi()
diwali=Diwali()
service=DiscountService(diwali)
service.process()
service.set_strategy(holi)
service.process()