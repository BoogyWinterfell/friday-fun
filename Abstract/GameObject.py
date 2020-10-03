from dataclasses import dataclass

from Abstract.NamedObject import NamedObject


@dataclass
class GameObject(NamedObject):
    owner_name: str
