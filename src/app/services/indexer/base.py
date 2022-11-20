from abc import ABC, abstractmethod
from .. import entries


class BaseIndexer(ABC):
    @abstractmethod
    def index(self, geopos: entries.Geopos) -> entries.H3Indexes: ...
