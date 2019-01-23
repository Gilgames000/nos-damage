import sys
from glob import glob

from PySide2 import QtWidgets

import util.persistence as ps
from datastructs.constants import Element
from datastructs.constants import MobType
from gui import Ui_MainWindow


def sort_entities(entities):
    entities.sort(key=lambda x: x.name)


def load_entities():
    entity_filenames = glob("entities/*.json")
    entities = [ps.load_entity(filename=fn) for fn in entity_filenames]
    sort_entities(entities)

    return entities


def setup_btn_listeners():
    # Editor entity

    # Editor stacked
    ui.btn_shell_effects.clicked.connect(
        lambda: ui.stacked_editor.setCurrentIndex(1)
    )
    ui.btn_shell_back.clicked.connect(
        lambda: ui.stacked_editor.setCurrentIndex(0)
    )
    ui.btn_other_effects.clicked.connect(
        lambda: ui.stacked_editor.setCurrentIndex(2)
    )
    ui.btn_other_back.clicked.connect(
        lambda: ui.stacked_editor.setCurrentIndex(0)
    )


def display_editor_entity(index):
    entity = entities[index]

    # Base
    ui.le_name.setText(entity.name)
    ui.sb_level.setValue(entity.level)
    ui.sb_fairy.setValue(entity.fairy)
    ui.cb_is_mage.setChecked(entity.is_mage)
    ui.cb_is_mob.setChecked(entity.is_mob)
    if entity.is_mob:
        ui.dropdown_mob_type.setEnabled(True)
        ui.dropdown_mob_type.setCurrentIndex(entity.mob_type)
    else:
        ui.dropdown_mob_type.setEnabled(False)
        ui.dropdown_mob_type.setCurrentIndex(MobType.NONE)
    ui.sb_atk_base.setValue(entity.atk_base)
    ui.sb_atk_equip_min.setValue(entity.atk_equip_min)
    ui.sb_atk_equip_max.setValue(entity.atk_equip_max)
    ui.sb_weapon_up.setValue(entity.weapon_up)
    ui.sb_crit_dmg_eq.setValue(entity.crit_dmg_eq)

    # Weapon
    ui.sb_atk_equip_min.setValue(entity.atk_equip_min)
    ui.sb_atk_equip_max.setValue(entity.atk_equip_max)
    ui.sb_res_reduction.setValue(entity.res_reduction)
    ui.sb_dmg_increase_eq.setValue(entity.dmg_increase_eq)
    ui.sb_dmg_increase_eq_prob.setValue(entity.dmg_increase_eq_prob)
    ui.sb_crit_dmg_eq.setValue(entity.crit_dmg_eq)
    ui.sb_crit_prob_eq.setValue(entity.crit_prob_eq)
    ui.sb_weapon_up.setValue(entity.weapon_up)

    # Armor
    ui.sb_def_base.setValue(entity.def_base)
    ui.sb_def_equip.setValue(entity.def_equip)
    ui.sb_crit_dmg_reduction.setValue(entity.crit_dmg_reduction)
    # ui.sb_crit_prob_reduction.setValue(entity.crit_prob_reduction)
    ui.sb_armor_up.setValue(entity.armor_up)

    # Weapon shell
    ui.sb_dmg_enhanced.setValue(entity.dmg_enhanced)
    ui.sb_dmg_increase_s.setValue(entity.dmg_increase_s)
    ui.sb_crit_dmg_shell.setValue(entity.crit_dmg_shell)
    ui.sb_dmg_increase_pvp.setValue(entity.dmg_increase_pvp)
    ui.sb_def_reduction_pvp.setValue(entity.def_reduction_pvp)
    ui.sb_res_reduction_pvp.setValue(entity.res_reduction_pvp)
    ui.sb_ele_prop_increase.setValue(entity.ele_prop_increase)
    ui.sb_dmg_increase_low_society.setValue(entity.dmg_increase_low_society)
    ui.sb_dmg_increase_evil.setValue(entity.dmg_increase_evil)
    ui.sb_dmg_increase_undead.setValue(entity.dmg_increase_undead)
    ui.sb_dmg_increase_plant.setValue(entity.dmg_increase_plant)
    ui.sb_dmg_increase_large.setValue(entity.dmg_increase_large)
    ui.sb_dmg_increase_animal.setValue(entity.dmg_increase_animal)

    # Armor shell
    ui.sb_def_enhanced.setValue(entity.def_enhanced)
    ui.sb_def_increase_s.setValue(entity.def_increase_s)
    ui.sb_def_increase_pvp.setValue(entity.def_increase_pvp)

    # SP
    ui.sb_atk_sp_points.setValue(entity.sp_build[0])
    ui.sb_atk_sp_pp.setValue(entity.atk_sp_pp)
    ui.sb_def_sp_points.setValue(entity.sp_build[1])
    ui.sb_def_sp_pp.setValue(entity.def_sp_pp)
    ui.sb_ele_sp_points.setValue(entity.sp_build[2])
    ui.sb_ele_sp_pp.setValue(entity.ele_sp_pp)
    ui.sb_hp_sp_points.setValue(entity.sp_build[3])
    # ui.sb_hp_sp_pp.setValue(entity.hp_sp_pp)

    # Other attack
    ui.sb_atk_effects.setValue(entity.atk_effects)
    ui.sb_ele_effects.setValue(entity.ele_effects)
    ui.cb_atk_oil.setChecked(entity.atk_oil)
    ui.cb_atk_pot.setChecked(entity.atk_pot)
    ui.sb_atk_hat.setValue(entity.atk_hat)
    ui.sb_atk_pet.setValue(entity.atk_pet)
    ui.sb_atk_pvp_hono.setValue(entity.atk_pvp_hono)
    ui.sb_atk_pvp_book.setValue(entity.atk_pvp_book)

    # Other defense
    ui.sb_def_effects.setValue(entity.def_effects)
    ui.sb_def_skill.setValue(entity.def_skill)
    ui.cb_def_oil.setChecked(entity.def_oil)
    ui.cb_def_pot.setChecked(entity.def_pot)
    ui.sb_def_costume.setValue(entity.def_costume)
    ui.sb_def_pet.setValue(entity.def_pet)
    ui.sb_def_pet_pvp.setValue(entity.def_pet_pvp)
    ui.sb_def_pvp_hono.setValue(entity.def_pvp_hono)
    ui.sb_def_pvp_book.setValue(entity.def_pvp_book)

    # Element
    ui.sb_fairy.setValue(entity.fairy)
    ui.dropdown_element.setCurrentIndex(entity.type)
    ui.sb_res.setValue(entity.res)

    # Buffs
    ui.sb_morale_bonus.setValue(entity.morale_bonus)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    entities = load_entities()

    ui.dropdown_entity.addItems([entity.name for entity in entities])
    ui.dropdown_element.addItems([element.name.lower() for element in Element])
    ui.dropdown_mob_type.addItems([mtype.name.lower() for mtype in MobType])

    ui.cb_is_mob.clicked.connect(
        lambda checked: ui.dropdown_mob_type.setEnabled(checked)
    )

    ui.dropdown_entity.currentIndexChanged.connect(display_editor_entity)

    ui.stacked_editor.setCurrentIndex(0)
    setup_btn_listeners()
    display_editor_entity(0)

    for i in entities:
        print(i)

    main_window.show()
    sys.exit(app.exec_())
