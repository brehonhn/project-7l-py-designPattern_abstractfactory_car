from abc import ABC, abstractmethod


class Coupe(ABC):
    @abstractmethod
    def specs(self):
        pass