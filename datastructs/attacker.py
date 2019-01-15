from dataclasses import dataclass

from typed_json_dataclass import TypedJsonMixin

import util.sptools as sp


@dataclass
class Attacker(TypedJsonMixin):
    # Base
    atk_base: int = 0
    level: int = 1

    # Gear
    atk_equip_min: int = 0
    atk_equip_max: int = 0
    res_reduction: int = 0
    dmg_increase_eq: int = 0
    dmg_increase_eq_prob: int = 0
    crit_dmg: int = 100
    crit_prob: int = 10
    up: int = 0

    # Shell
    dmg_enhanced: int = 0
    dmg_increase_s: int = 0
    dmg_increase_pvp: int = 0
    def_reduction_pvp: int = 0
    res_reduction_pvp: int = 0
    ele_prop_increase: int = 0

    # SP
    _sp_build = [0, 0, 0, 0]
    atk_sp_build: int = 0
    atk_sp_pp: int = 0
    atk_sp_bonus: int = 0
    atk_skill: int = 0
    ele_sp_build: int = 0
    ele_sp_pp: int = 0
    ele_sp_bonus: int = 0
    ele_skill: int = 0

    # Other
    atk_effects: int = 0
    ele_effects: int = 0
    atk_oil: bool = False
    atk_pot: bool = False
    atk_hat: int = 0
    atk_pet: int = 0
    atk_pvp_hono: int = 0
    atk_pvp_book: int = 0
    morale_bonus: int = 0

    # Element
    fairy: int = 0
    type: str = "no_elem"

    # Mob
    is_mob: bool = False

    def __post_init__(self):
        self._update_build()

    @property
    def sp_build(self):
        return self._sp_build

    @sp_build.setter
    def sp_build(self, build):
        self._sp_build = build
        self._update_build()

    def atk_sp(self):
        return (self.atk_sp_build
                + self.atk_sp_bonus
                + self.atk_sp_pp)

    def ele_sp(self):
        return (self.ele_sp_build
                + self.ele_sp_bonus
                + self.ele_sp_pp)

    def morale(self):
        return self.level + self.morale_bonus

    def mob_damage(self):
        dmg = 0
        # TODO: implement mob damage formula

        return int(self.is_mob) * dmg

    def _update_build(self):
        self.atk_sp_build = sp.atk_base_build(build=self._sp_build)
        self.atk_sp_bonus = sp.atk_bonus_build(build=self._sp_build)
        self.ele_sp_build = sp.ele_base_build(build=self._sp_build)
        self.ele_sp_bonus = sp.ele_bonus_build(build=self._sp_build)
