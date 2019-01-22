from enum import IntEnum

equip_up_bonus = [0, 0.1, 0.15, 0.22, 0.32, 0.43, 0.54, 0.65, 0.9, 1.2, 2]

sp_up_bonus = [0, 5, 10, 15, 20, 28, 36, 46, 56, 68, 80, 95, 110, 128, 148,
               173]

type_matchups = {
    "FIRE>WATER": 1,
    "WATER>FIRE": 1,
    "LIGHT>SHADOW": 2,
    "SHADOW>LIGHT": 2,
    "FIRE>SHADOW": 0.5,
    "SHADOW>WATER": 0.5,
    "WATER>LIGHT": 0.5,
    "LIGHT>FIRE": 0.5,
    "FIRE>NO_ELEMENT": 0.3,
    "WATER>NO_ELEMENT": 0.3,
    "LIGHT>NO_ELEMENT": 0.3,
    "SHADOW>NO_ELEMENT": 0.3
}


def elemental_bonus(matchup):
    return type_matchups.get(matchup, 0)


class Element(IntEnum):
    NO_ELEMENT = 0
    LIGHT = 1
    SHADOW = 2
    WATER = 3
    FIRE = 4


class DamageType(IntEnum):
    ALL = 0
    NORMAL = 1
    SOFT = 2
    CRIT = 3
    SOFTCRIT = 4


class MobType(IntEnum):
    NONE = 0
    LOW_SOCIETY = 1
    EVIL = 2
    UNDEAD = 3
    PLANT = 4
    LARGE = 5
    ANIMAL = 6
