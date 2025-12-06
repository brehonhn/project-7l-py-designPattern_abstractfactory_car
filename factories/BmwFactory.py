from factories.CarFactory import CarFactory
from products.coupe.BmwCoupe import BmwCoupe
from products.coupe.Coupe import Coupe
from products.suv.BmwSUV import BmwSUV
from products.suv.SUV import SUV


class BmwFactory(CarFactory):
    def create_suv(self) -> SUV:
        return BmwSUV()

    def create_coupe(self) -> Coupe:
        return BmwCoupe()