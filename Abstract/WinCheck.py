import abc
from typing import List

from Abstract.EngineGameInfo import EngineGameInfo


class WinCheck(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search_for_winners(self, info: EngineGameInfo) -> List[str]:
        pass
