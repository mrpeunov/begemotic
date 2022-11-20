from abc import ABC, abstractmethod
import entries


class BaseHouseRepo(ABC):
    @abstractmethod
    def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses: ...
