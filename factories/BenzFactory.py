from factories.CarFactory import CarFactory
from products.coupe.BenzCoupe import BenzCoupe
from products.coupe.Coupe import Coupe
from products.suv.BenzSUV import BenzSUV
from products.suv.SUV import SUV


class BenzFactory(CarFactory):
    def create_suv(self) -> SUV:
        return BenzSUV()

    def create_coupe(self) -> Coupe:
        return BenzCoupe()
