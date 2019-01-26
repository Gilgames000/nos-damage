from noscalculator.calculator import Calculator


class CalculatorController:
    def __init__(self, ui, entities):
        self.ui = ui
        self.entities = entities
        self.populate_dropdowns()
        self.initialize_damage_labels()
        self.setup_btn_listeners()
        self.attacker = self.entities[0]
        self.defender = self.entities[0]
        self.ui.cb_calc_multiple_defenders.setEnabled(False)
        self.ui.btn_calc_select_defenders.setEnabled(False)

    def update(self, entities, args):
        entity_names = [entity.name for entity in entities]

        self.ui.dropdown_calc_attacker.clear()
        self.ui.dropdown_calc_attacker.addItems(entity_names)
        self.ui.dropdown_calc_defender.clear()
        self.ui.dropdown_calc_defender.addItems(entity_names)

    def populate_dropdowns(self):
        entity_names = [entity.name for entity in self.entities]

        self.ui.dropdown_calc_attacker.addItems(entity_names)
        self.ui.dropdown_calc_defender.addItems(entity_names)

    def initialize_damage_labels(self):
        self.ui.lb_calc_normal_max.setText("0")
        self.ui.lb_calc_normal_min.setText("0")
        self.ui.lb_calc_crit_max.setText("0")
        self.ui.lb_calc_crit_min.setText("0")
        self.ui.lb_calc_soft_max.setText("0")
        self.ui.lb_calc_soft_min.setText("0")
        self.ui.lb_calc_softcrit_max.setText("0")
        self.ui.lb_calc_softcrit_min.setText("0")
        self.ui.lb_calc_average.setText("0")

    def setup_btn_listeners(self):
        self.ui.btn_calculate.clicked.connect(self.calculate)

        self.ui.dropdown_calc_attacker.currentIndexChanged.connect(
            self.select_attacker
        )
        self.ui.dropdown_calc_defender.currentIndexChanged.connect(
            self.select_defender
        )

    def select_attacker(self):
        idx = self.ui.dropdown_calc_attacker.currentIndex()
        self.attacker = self.entities[idx]

    def select_defender(self):
        idx = self.ui.dropdown_calc_defender.currentIndex()
        self.defender = self.entities[idx]

    def calculate(self):
        self.attacker.atk_skill = self.ui.sb_calc_atk_skill.value()
        self.attacker.ele_skill = self.ui.sb_calc_ele_skill.value()
        calculator = Calculator(self.attacker, self.defender)

        normal_min, normal_max = calculator.damage()
        crit_min, crit_max = calculator.damage(crit=True)
        soft_min, soft_max = calculator.damage(soft=True)
        softcrit_min, softcrit_max = calculator.damage(crit=True, soft=True)
        average_damage = calculator.average_damage()

        self.ui.lb_calc_normal_max.setText(str(normal_max))
        self.ui.lb_calc_normal_min.setText(str(normal_min))
        self.ui.lb_calc_crit_max.setText(str(crit_max))
        self.ui.lb_calc_crit_min.setText(str(crit_min))
        self.ui.lb_calc_soft_max.setText(str(soft_max))
        self.ui.lb_calc_soft_min.setText(str(soft_min))
        self.ui.lb_calc_softcrit_max.setText(str(softcrit_max))
        self.ui.lb_calc_softcrit_min.setText(str(softcrit_min))
        self.ui.lb_calc_average.setText(str(average_damage))
