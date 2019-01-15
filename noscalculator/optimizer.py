import util.sptools as sp
from noscalculator import Calculator


class Optimizer:
    def __init__(self, attacker, defender, job=99, up=15):
        if not 0 <= job <= 99:
            raise ValueError("SP job must be an integer between 0 and 99")
        if not 0 <= up <= 15:
            raise ValueError("SP up must be an integer between 0 and 15")

        self.calculator = Calculator(attacker, defender)
        self.attacker = attacker
        self.defender = defender
        self.job = job
        self.up = up

    def is_build_valid(self, x):
        return sp.validate_build(self.job, self.up, [x[0], 0, x[1], 0])

    def target(self, x):
        self.calculator.attacker.sp_build = [x[0], 0, x[1], 0]
        return self.calculator.average_damage()

    def maximize_damage(self):
        # Update calculator just in case it changed
        self.calculator = Calculator(self.attacker, self.defender)

        valid_builds = [
            (i, j)
            for i in range(0, 101)
            for j in range(0, 101)
            if self.is_build_valid((i, j))
        ]

        result = list(zip(valid_builds, map(self.target, valid_builds)))
        result.sort(key=lambda x: x[1], reverse=True)

        return result
