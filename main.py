from datastructs import Entity
from datastructs.constants import DamageType
from datastructs.constants import MobType
from noscalculator import Calculator
from noscalculator import Optimizer
import util.persistence as ps


def main():
    attacker = Entity()
    defender = Entity()

    attacker.is_mage = True
    attacker.dmg_increase_pvp = 0
    attacker.is_mob = False
    defender.def_base = 200
    defender.def_increase_pvp = 50
    defender.is_mob = True
    attacker.dmg_increase_evil = 16
    defender.mob_type = MobType.EVIL

    calc = Calculator(attacker, defender)
    opt = Optimizer(attacker, defender)

    # print("before", attacker.sp_build)
    # r = opt.maximize_damage(target_dmg=DamageType.ALL, atk_sl=18, ele_sl=18)
    # for i in range(30):
    #     print(r[i])
    # print("after", attacker.sp_build)

    attacker.name = "Attacker"
    ps.save_entity(attacker, "entities/attacker.json")
    defender.name = "Defender"
    ps.save_entity(defender, "./entities/defender.json")

    attacker.sp_build = [0, 10, 84, 22]
    print(attacker.crit_dmg(), attacker.crit_prob())
    attacker.sp_build = [40, 10, 84, 22]
    print(attacker.crit_dmg(), attacker.crit_prob())
    attacker.sp_build = [90, 10, 84, 22]
    print(attacker.crit_dmg(), attacker.crit_prob())
    attacker.sp_build = [100, 10, 84, 22]
    print(attacker.crit_dmg(), attacker.crit_prob())
    print(calc.damage(average=True))
    print(calc.damage(average=True, soft=True))
    print(calc.damage(average=False, crit=True))
    print(calc.damage(average=True, soft=True, crit=True))
    print(calc.average_damage())


if __name__ == "__main__":
    main()
