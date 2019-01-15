from dataclasses import dataclass

from typed_json_dataclass import TypedJsonMixin

import util.sptools as sp


@dataclass
class Defender(TypedJsonMixin):
    # Base
    def_base: int = 0
    level: int = 1

    # Gear
    def_equip: int = 0
    crit_dmg_reduction: int = 0
    crit_prob_reduction: int = 10
    up: int = 0

    # Shell
    def_enhanced: int = 0
    def_increase_s: int = 0
    def_increase_pvp: int = 0

    # SP
    _sp_build = [0, 0, 0, 0]
    def_sp_build: int = 0
    def_sp_pp: int = 0
    def_sp_bonus: int = 0
    magic_dmg_reduction: int = 0

    # Other
    def_effects: int = 0
    def_skill: int = 0
    def_oil: bool = False
    def_pot: bool = False
    def_costume: int = 0
    def_pet: int = 0
    def_pet_pvp: int = 0
    def_pvp_hono: int = 0
    def_pvp_book: int = 0
    morale_bonus: int = 0

    # Element
    res: int = 0
    type: str = "no_elem"

    def __post_init__(self):
        self._update_build()

    @property
    def sp_build(self):
        return self._sp_build

    @sp_build.setter
    def sp_build(self, build):
        self._sp_build = build
        self._update_build()

    def def_sp(self):
        return (self.def_sp_build
                + self.def_sp_bonus
                + self.def_sp_pp)

    def morale(self):
        return self.level + self.morale_bonus

    def _update_build(self):
        self.atk_sp_build = sp.atk_base_build(build=self._sp_build)
        self.atk_sp_bonus = sp.atk_bonus_build(build=self._sp_build)
        self.ele_sp_build = sp.ele_base_build(build=self._sp_build)
        self.ele_sp_bonus = sp.ele_bonus_build(build=self._sp_build)
