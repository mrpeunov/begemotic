from abc import ABC, abstractmethod
from . import entries


class BaseHouseRepo(ABC):
    @abstractmethod
    async def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses: ...
