import abc
from dataclasses import dataclass

from Abstract.NamedObject import NamedObject


@dataclass
class BotInfo(NamedObject, metaclass=abc.ABCMeta):
    pass
