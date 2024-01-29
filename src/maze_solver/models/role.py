# models/role.py

from enum import IntEnum, auto


class Role(IntEnum):
    NONE = 0
    ENEMY = auto()  # members of enumaration, indicated by caps
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()
