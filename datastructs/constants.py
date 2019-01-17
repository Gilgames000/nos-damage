from enum import Enum

equip_up_bonus = [0, 0.1, 0.15, 0.22, 0.32, 0.43, 0.54, 0.65, 0.9, 1.2, 2]

sp_up_bonus = [0, 5, 10, 15, 20, 28, 36, 46, 56, 68, 80, 95, 110, 128, 148,
               173]

type_matchups = {
    "fire>water": 1,
    "water>fire": 1,
    "light>shadow": 2,
    "shadow>light": 2,
    "fire>shadow": 0.5,
    "shadow>water": 0.5,
    "water>light": 0.5,
    "light>fire": 0.5,
    "fire>no_elem": 0.3,
    "water>no_elem": 0.3,
    "light>no_elem": 0.3,
    "shadow>no_elem": 0.3
}


def elemental_bonus(matchup):
    return type_matchups.get(matchup, 0)


class DamageType(Enum):
    ALL = 1
    NORMAL = 2
    SOFT = 3
    CRIT = 4
    SOFTCRIT = 5
