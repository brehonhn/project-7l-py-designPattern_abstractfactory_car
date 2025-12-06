from abc import ABC, abstractmethod

from products.coupe.Coupe import Coupe
from products.suv.SUV import SUV


class CarFactory(ABC):
    @abstractmethod
    def create_suv(self) -> SUV:
        pass

    @abstractmethod
    def create_coupe(self) -> Coupe:
        pass