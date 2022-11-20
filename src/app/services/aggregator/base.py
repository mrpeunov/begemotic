from abc import ABC, abstractmethod
from ..entries import Houses, AggrResult


class BaseAggregator(ABC):
    @abstractmethod
    def aggregate(self, houses: Houses) -> AggrResult: ...
