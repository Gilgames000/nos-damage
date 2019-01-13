from datastructs import Attacker
from datastructs import Defender
from noscalculator import Calculator
from util import persistence as ps


def main():
    attacker = Attacker()
    defender = Defender()
    calc = Calculator(attacker, defender)

    ps.save_attacker(attacker, "attacker.json")
    ps.save_defender(defender, "defender.json")

    print(calc.damage())


if __name__ == "__main__":
    main()
