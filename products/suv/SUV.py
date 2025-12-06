from abc import ABC, abstractmethod


class SUV(ABC):
    @abstractmethod
    def specs(self):
        pass