from math import floor

from datastructs.constants import elemental_bonus
from datastructs.constants import equip_up_bonus
from datastructs import MobType


class Calculator:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def atk_tot(self, atk_eq, soft=False):
        is_pvp = int(
            not self.attacker.is_mob
            and not self.defender.is_mob
        )
        up = min(max(self.attacker.weapon_up - self.defender.armor_up, 0), 10)

        atk_char = (
                (atk_eq * (1 + equip_up_bonus[up])
                 + self.attacker.atk_base
                 + self.attacker.atk_effects
                 + self.attacker.atk_sp()
                 + self.attacker.dmg_enhanced)
                * (1 + is_pvp * self.attacker.dmg_increase_pvp / 100)
        )

        mob_type_dmg = 0
        if self.defender.is_mob:
            if self.defender.mob_type == MobType.LOW_SOCIETY:
                mob_type_dmg = self.attacker.dmg_increase_low_society
            elif self.defender.mob_type == MobType.EVIL:
                mob_type_dmg = self.attacker.dmg_increase_evil
            elif self.defender.mob_type == MobType.UNDEAD:
                mob_type_dmg = self.attacker.dmg_increase_undead
            elif self.defender.mob_type == MobType.PLANT:
                mob_type_dmg = self.attacker.dmg_increase_plant
            elif self.defender.mob_type == MobType.LARGE:
                mob_type_dmg = self.attacker.dmg_increase_large
            elif self.defender.mob_type == MobType.ANIMAL:
                mob_type_dmg = self.attacker.dmg_increase_animal

        return (
                (atk_char + self.attacker.atk_skill + 15)
                * (1 + self.attacker.dmg_increase_s + mob_type_dmg / 100)
                * (1 + self.attacker.dmg_increase_eq / 100 * int(soft))
        )

    def def_tot(self):
        is_pvp = int(
            not self.attacker.is_mob
            and not self.defender.is_mob
        )
        up = min(max(self.defender.armor_up - self.attacker.weapon_up, 0), 10)

        def_char = (
                (self.defender.def_equip * (1 + equip_up_bonus[up])
                 + self.defender.def_base
                 + self.defender.def_effects
                 + self.defender.def_sp()
                 + self.defender.def_enhanced)
                * (1 + (self.defender.def_increase_s
                        + is_pvp * self.defender.def_increase_pvp
                        - is_pvp * self.attacker.def_reduction_pvp) / 100)
        )

        return (
                (def_char + self.defender.def_skill)
                * (1 + is_pvp * self.defender.def_pet_pvp / 100)
                * (1 + (int(self.defender.def_pot) * 20
                        + int(self.defender.def_oil) * 5
                        + self.defender.def_costume
                        + self.defender.def_pet) / 100)
        )

    def atk_ele_tot(self, atk_eq, soft=False):
        atk_ele = (
                (self.atk_tot(atk_eq, soft=soft) + 100)
                * (self.attacker.fairy + self.attacker.ele_sp()) / 100
        )

        return (
                atk_ele
                + self.attacker.ele_skill
                + self.attacker.ele_effects
                + self.attacker.ele_prop_increase
        )

    def physical_damage(self, atk_eq, crit=False, soft=False):
        dmg = (
                (self.atk_tot(atk_eq, soft=soft) - self.def_tot())
                * (1 + int(self.attacker.atk_oil) * 0.05)
        )

        if crit:
            dmg *= (
                    1 + self.attacker.crit_dmg() / 100
                    - self.defender.crit_dmg_reduction / 100
            )

        return dmg

    def elemental_damage(self, atk_eq, soft=False):
        is_pvp = int(
            not self.attacker.is_mob
            and not self.defender.is_mob
        )
        matchup = f"{self.attacker.type}>{self.defender.type}"
        res = (
                self.defender.res
                - self.attacker.res_reduction
                - is_pvp * self.attacker.res_reduction_pvp
        )

        return (
                self.atk_ele_tot(atk_eq, soft=soft)
                * (1 + elemental_bonus(matchup))
                * (1 - res / 100)
        )

    def final_damage(self, atk_eq, crit=False, soft=False, no_ele=False,
                     is_min=False, max_crit_dmg=0):
        is_pvp = int(
            not self.attacker.is_mob
            and not self.defender.is_mob
        )
        morale = self.attacker.morale() - self.defender.morale()

        if no_ele:
            elemental_damage = 0
        else:
            elemental_damage = self.elemental_damage(atk_eq, soft=soft)

        physical_damage = self.physical_damage(atk_eq, crit=crit, soft=soft)

        if crit and is_min:
            physical_damage = (physical_damage + max_crit_dmg) / 2

        dmg = (
                morale
                + physical_damage
                + elemental_damage
                + self.attacker.mob_damage()
        )

        dmg *= (
                (1 + is_pvp * self.attacker.atk_pvp_book / 100)
                * (1 + is_pvp * self.attacker.atk_pvp_hono / 100)
                * (1 - is_pvp * self.defender.def_pvp_book / 100)
                * (1 - is_pvp * self.defender.def_pvp_hono / 100)
                * (1 - self.defender.magic_dmg_reduction / 100)
                * (1 + (self.attacker.atk_hat
                        + self.attacker.atk_pet
                        + int(self.attacker.atk_pot) * 20) / 100)
        )

        return dmg

    def damage(self, crit=False, soft=False, no_ele=False, average=False):
        dmg_max = self.final_damage(
            self.attacker.atk_equip_max,
            crit=crit,
            soft=soft,
            no_ele=no_ele
        )

        if crit:
            max_crit_dmg = self.physical_damage(
                self.attacker.atk_equip_max,
                crit=crit,
                soft=soft
            )
        else:
            max_crit_dmg = 0

        dmg_min = self.final_damage(
            self.attacker.atk_equip_min,
            crit=crit,
            soft=soft,
            no_ele=no_ele,
            is_min=True,
            max_crit_dmg=max_crit_dmg
        )

        dmg_min = max(dmg_min, 1)
        dmg_max = max(dmg_max, 5)

        if average:
            return (dmg_min + dmg_max) / 2

        return floor(dmg_min), floor(dmg_max)

    def average_damage(self):
        soft = self.attacker.dmg_increase_eq_prob / 100
        crit = self.attacker.crit_prob() / 100
        soft_crit = soft / 100 * crit / 100
        normal = 1 - soft - crit - soft_crit

        return (
                self.damage(average=True) * normal
                + self.damage(average=True, soft=True) * soft
                + self.damage(average=True, crit=True) * crit
                + self.damage(average=True, soft=True, crit=True) * soft_crit
        )

    def swap_attacker_defender(self):
        tmp = self.attacker
        self.attacker = self.defender
        self.defender = tmp
