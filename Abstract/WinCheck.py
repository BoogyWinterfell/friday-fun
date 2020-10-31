import abc
from typing import List

from Abstract.GameInfo import GameInfo


class WinCheck(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search_for_winners(self, info: GameInfo) -> List[str]:
        pass
