from abc import ABC, abstractmethod


class Aconfig(ABC):
    @abstractmethod
    def copy(self):
        pass
