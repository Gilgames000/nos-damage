import util.persistence as ps
from datastructs import Entity
from datastructs.constants import Element
from datastructs.constants import MobType


class EditorController:
    def __init__(self, ui, entities):
        self.ui = ui
        self.entities = entities
        self.sort_entities()
        self.populate_dropdowns()
        self.setup_btn_listeners()
        self.display_editor_entity(0)

    def sort_entities(self):
        self.entities.sort(key=lambda x: x.name)

    def entity_exists(self, name):
        return True in map(lambda e: name == e.name, self.entities)

    def add_entity(self, entity, sort=True):
        self.entities.append(entity)
        if sort:
            self.sort_entities()
            pos = self.entities.index(entity)
        else:
            pos = max(0, len(self.entities) - 1)

        return pos

    def disable_editor_buttons(self):
        self.ui.btn_new.setDisabled(True)
        self.ui.btn_save.setDisabled(True)
        self.ui.btn_duplicate.setDisabled(True)
        self.ui.btn_delete.setDisabled(True)

    def enable_editor_buttons(self):
        self.ui.btn_new.setDisabled(False)
        self.ui.btn_save.setDisabled(False)
        self.ui.btn_duplicate.setDisabled(False)
        self.ui.btn_delete.setDisabled(False)

    def add_dupe_suffix(self, name):
        dupes = 1
        while self.entity_exists(name):
            name = f"{name}_{dupes}"
            dupes += 1

        return name

    def duplicate_entity(self):
        from time import time_ns
        self.disable_editor_buttons()

        current_entity = self.entities[self.ui.dropdown_entity.currentIndex()]
        new_entity = ps.load_entity(f"entities/{current_entity.filename}.json")
        name = current_entity.name
        # name = self.add_dupe_suffix(current_entity.name)
        new_entity.filename = time_ns()
        new_entity.name = name
        pos = self.add_entity(new_entity)

        self.ui.dropdown_entity.insertItem(pos, name)
        self.ui.dropdown_entity.setCurrentIndex(pos)

        self.save_entity()

        self.enable_editor_buttons()

    def new_entity(self):
        from datastructs import Entity

        self.disable_editor_buttons()

        name = "no_name"
        # name = self.add_dupe_suffix("no_name")

        entity = Entity(name=name)
        pos = self.add_entity(entity)

        self.ui.dropdown_entity.insertItem(pos, name)
        self.ui.dropdown_entity.setCurrentIndex(pos)

        self.save_entity()

        self.enable_editor_buttons()

    def save_entity(self):
        from os import path, mkdir
        self.disable_editor_buttons()

        idx = self.ui.dropdown_entity.currentIndex()
        entity = self.entities[idx]

        # Base
        entity.name = self.ui.le_name.text()
        entity.level = self.ui.sb_level.value()
        entity.fairy = self.ui.sb_fairy.value()
        entity.is_mage = self.ui.cb_is_mage.isChecked()
        entity.is_mob = self.ui.cb_is_mob.isChecked()
        entity.mob_type = self.ui.dropdown_mob_type.currentIndex()
        entity.atk_base = self.ui.sb_atk_base.value()
        entity.atk_equip_min = self.ui.sb_atk_equip_min.value()
        entity.atk_equip_max = self.ui.sb_atk_equip_max.value()
        entity.weapon_up = self.ui.sb_weapon_up.value()
        entity.crit_dmg_eq = self.ui.sb_crit_dmg_eq.value()

        # Weapon
        entity.atk_equip_min = self.ui.sb_atk_equip_min.value()
        entity.atk_equip_max = self.ui.sb_atk_equip_max.value()
        entity.res_reduction = self.ui.sb_res_reduction.value()
        entity.dmg_increase_eq = self.ui.sb_dmg_increase_eq.value()
        entity.dmg_increase_eq_prob = self.ui.sb_dmg_increase_eq_prob.value()
        entity.crit_dmg_eq = self.ui.sb_crit_dmg_eq.value()
        entity.crit_prob_eq = self.ui.sb_crit_prob_eq.value()
        entity.weapon_up = self.ui.sb_weapon_up.value()

        # Armor
        entity.def_base = self.ui.sb_def_base.value()
        entity.def_equip = self.ui.sb_def_equip.value()
        entity.crit_dmg_reduction = self.ui.sb_crit_dmg_reduction.value()
        entity.armor_up = self.ui.sb_armor_up.value()

        # Weapon shell
        entity.dmg_enhanced = self.ui.sb_dmg_enhanced.value()
        entity.dmg_increase_s = self.ui.sb_dmg_increase_s.value()
        entity.crit_dmg_shell = self.ui.sb_crit_dmg_shell.value()
        entity.dmg_increase_pvp = self.ui.sb_dmg_increase_pvp.value()
        entity.def_reduction_pvp = self.ui.sb_def_reduction_pvp.value()
        entity.res_reduction_pvp = self.ui.sb_res_reduction_pvp.value()
        entity.ele_prop_increase = self.ui.sb_ele_prop_increase.value()
        entity.dmg_increase_low_society = self.ui.sb_dmg_increase_low_society.value()
        entity.dmg_increase_evil = self.ui.sb_dmg_increase_evil.value()
        entity.dmg_increase_undead = self.ui.sb_dmg_increase_undead.value()
        entity.dmg_increase_plant = self.ui.sb_dmg_increase_plant.value()
        entity.dmg_increase_large = self.ui.sb_dmg_increase_large.value()
        entity.dmg_increase_animal = self.ui.sb_dmg_increase_animal.value()

        # Armor shell
        entity.def_enhanced = self.ui.sb_def_enhanced.value()
        entity.def_increase_s = self.ui.sb_def_increase_s.value()
        entity.def_increase_pvp = self.ui.sb_def_increase_pvp.value()

        # SP
        entity.sp_build = (
            self.ui.sb_atk_sp_points.value(),
            self.ui.sb_def_sp_points.value(),
            self.ui.sb_ele_sp_points.value(),
            self.ui.sb_hp_sp_points.value()
        )
        entity.atk_sp_pp = self.ui.sb_atk_sp_pp.value()
        entity.def_sp_pp = self.ui.sb_def_sp_pp.value()
        entity.ele_sp_pp = self.ui.sb_ele_sp_pp.value()

        # Other attack
        entity.atk_effects = self.ui.sb_atk_effects.value()
        entity.ele_effects = self.ui.sb_ele_effects.value()
        entity.atk_oil = self.ui.cb_atk_oil.isChecked()
        entity.atk_pot = self.ui.cb_atk_pot.isChecked()
        entity.atk_hat = self.ui.sb_atk_hat.value()
        entity.atk_pet = self.ui.sb_atk_pet.value()
        entity.atk_pvp_hono = self.ui.sb_atk_pvp_hono.value()
        entity.atk_pvp_book = self.ui.sb_atk_pvp_book.value()

        # Other defense
        entity.def_effects = self.ui.sb_def_effects.value()
        entity.def_skill = self.ui.sb_def_skill.value()
        entity.def_oil = self.ui.cb_def_oil.isChecked()
        entity.def_pot = self.ui.cb_def_pot.isChecked()
        entity.def_costume = self.ui.sb_def_costume.value()
        entity.def_pet = self.ui.sb_def_pet.value()
        entity.def_pet_pvp = self.ui.sb_def_pet_pvp.value()
        entity.def_pvp_hono = self.ui.sb_def_pvp_hono.value()
        entity.def_pvp_book = self.ui.sb_def_pvp_book.value()

        # Element
        entity.fairy = self.ui.sb_fairy.value()
        entity.type = self.ui.dropdown_element.currentIndex()
        entity.res = self.ui.sb_res.value()

        # Buffs
        entity.morale_bonus = self.ui.sb_morale_bonus.value()

        if not path.isdir("entities"):
            mkdir("entities", 0o777)
        ps.save_entity(entity, f"entities/{entity.filename}.json")

        idx = self.ui.dropdown_entity.currentIndex()
        self.sort_entities()
        new_idx = self.entities.index(entity)
        self.ui.dropdown_entity.removeItem(idx)
        self.ui.dropdown_entity.insertItem(new_idx, entity.name)
        self.ui.dropdown_entity.setCurrentIndex(new_idx)
        self.display_editor_entity(new_idx)

        self.enable_editor_buttons()

    def delete_entity(self):
        self.disable_editor_buttons()

        idx = self.ui.dropdown_entity.currentIndex()
        self.ui.dropdown_entity.removeItem(idx)
        ps.delete_entity(f"entities/{self.entities[idx].filename}.json")
        self.entities.remove(self.entities[idx])

        self.display_editor_entity(idx - 1)
        self.enable_editor_buttons()

    def setup_btn_listeners(self):
        # Editor entity
        self.ui.btn_new.clicked.connect(self.new_entity)
        self.ui.btn_save.clicked.connect(self.save_entity)
        self.ui.btn_duplicate.clicked.connect(self.duplicate_entity)
        self.ui.btn_delete.clicked.connect(self.delete_entity)

        # Base
        self.ui.cb_is_mob.clicked.connect(
            lambda checked: self.ui.dropdown_mob_type.setEnabled(checked)
        )
        self.ui.dropdown_entity.currentIndexChanged.connect(
            self.display_editor_entity
        )

        # Editor stacked
        self.ui.btn_shell_effects.clicked.connect(
            lambda: self.ui.stacked_editor.setCurrentIndex(1)
        )
        self.ui.btn_shell_back.clicked.connect(
            lambda: self.ui.stacked_editor.setCurrentIndex(0)
        )
        self.ui.btn_other_effects.clicked.connect(
            lambda: self.ui.stacked_editor.setCurrentIndex(2)
        )
        self.ui.btn_other_back.clicked.connect(
            lambda: self.ui.stacked_editor.setCurrentIndex(0)
        )

    def populate_dropdowns(self):
        self.ui.dropdown_entity.addItems(
            [entity.name for entity in self.entities]
        )
        self.ui.dropdown_element.addItems(
            [element.name.lower() for element in Element]
        )
        self.ui.dropdown_mob_type.addItems(
            [mtype.name.lower() for mtype in MobType]
        )

    def display_editor_entity(self, index):
        self.guarantee_non_emptiness()

        entity = self.entities[index]

        # Base
        self.ui.le_name.setText(entity.name)
        self.ui.sb_level.setValue(entity.level)
        self.ui.sb_fairy.setValue(entity.fairy)
        self.ui.cb_is_mage.setChecked(entity.is_mage)
        self.ui.cb_is_mob.setChecked(entity.is_mob)
        if entity.is_mob:
            self.ui.dropdown_mob_type.setEnabled(True)
            self.ui.dropdown_mob_type.setCurrentIndex(entity.mob_type)
        else:
            self.ui.dropdown_mob_type.setEnabled(False)
            self.ui.dropdown_mob_type.setCurrentIndex(MobType.NONE)
        self.ui.sb_atk_base.setValue(entity.atk_base)
        self.ui.sb_atk_equip_min.setValue(entity.atk_equip_min)
        self.ui.sb_atk_equip_max.setValue(entity.atk_equip_max)
        self.ui.sb_weapon_up.setValue(entity.weapon_up)
        self.ui.sb_crit_dmg_eq.setValue(entity.crit_dmg_eq)

        # Weapon
        self.ui.sb_atk_equip_min.setValue(entity.atk_equip_min)
        self.ui.sb_atk_equip_max.setValue(entity.atk_equip_max)
        self.ui.sb_res_reduction.setValue(entity.res_reduction)
        self.ui.sb_dmg_increase_eq.setValue(entity.dmg_increase_eq)
        self.ui.sb_dmg_increase_eq_prob.setValue(entity.dmg_increase_eq_prob)
        self.ui.sb_crit_dmg_eq.setValue(entity.crit_dmg_eq)
        self.ui.sb_crit_prob_eq.setValue(entity.crit_prob_eq)
        self.ui.sb_weapon_up.setValue(entity.weapon_up)

        # Armor
        self.ui.sb_def_base.setValue(entity.def_base)
        self.ui.sb_def_equip.setValue(entity.def_equip)
        self.ui.sb_crit_dmg_reduction.setValue(entity.crit_dmg_reduction)
        # self.ui.sb_crit_prob_reduction.setValue(entity.crit_prob_reduction)
        self.ui.sb_armor_up.setValue(entity.armor_up)

        # Weapon shell
        self.ui.sb_dmg_enhanced.setValue(entity.dmg_enhanced)
        self.ui.sb_dmg_increase_s.setValue(entity.dmg_increase_s)
        self.ui.sb_crit_dmg_shell.setValue(entity.crit_dmg_shell)
        self.ui.sb_dmg_increase_pvp.setValue(entity.dmg_increase_pvp)
        self.ui.sb_def_reduction_pvp.setValue(entity.def_reduction_pvp)
        self.ui.sb_res_reduction_pvp.setValue(entity.res_reduction_pvp)
        self.ui.sb_ele_prop_increase.setValue(entity.ele_prop_increase)
        self.ui.sb_dmg_increase_low_society.setValue(
            entity.dmg_increase_low_society)
        self.ui.sb_dmg_increase_evil.setValue(entity.dmg_increase_evil)
        self.ui.sb_dmg_increase_undead.setValue(entity.dmg_increase_undead)
        self.ui.sb_dmg_increase_plant.setValue(entity.dmg_increase_plant)
        self.ui.sb_dmg_increase_large.setValue(entity.dmg_increase_large)
        self.ui.sb_dmg_increase_animal.setValue(entity.dmg_increase_animal)

        # Armor shell
        self.ui.sb_def_enhanced.setValue(entity.def_enhanced)
        self.ui.sb_def_increase_s.setValue(entity.def_increase_s)
        self.ui.sb_def_increase_pvp.setValue(entity.def_increase_pvp)

        # SP
        self.ui.sb_atk_sp_points.setValue(entity.sp_build[0])
        self.ui.sb_atk_sp_pp.setValue(entity.atk_sp_pp)
        self.ui.sb_def_sp_points.setValue(entity.sp_build[1])
        self.ui.sb_def_sp_pp.setValue(entity.def_sp_pp)
        self.ui.sb_ele_sp_points.setValue(entity.sp_build[2])
        self.ui.sb_ele_sp_pp.setValue(entity.ele_sp_pp)
        self.ui.sb_hp_sp_points.setValue(entity.sp_build[3])
        # self.ui.sb_hp_sp_pp.setValue(entity.hp_sp_pp)

        # Other attack
        self.ui.sb_atk_effects.setValue(entity.atk_effects)
        self.ui.sb_ele_effects.setValue(entity.ele_effects)
        self.ui.cb_atk_oil.setChecked(entity.atk_oil)
        self.ui.cb_atk_pot.setChecked(entity.atk_pot)
        self.ui.sb_atk_hat.setValue(entity.atk_hat)
        self.ui.sb_atk_pet.setValue(entity.atk_pet)
        self.ui.sb_atk_pvp_hono.setValue(entity.atk_pvp_hono)
        self.ui.sb_atk_pvp_book.setValue(entity.atk_pvp_book)

        # Other defense
        self.ui.sb_def_effects.setValue(entity.def_effects)
        self.ui.sb_def_skill.setValue(entity.def_skill)
        self.ui.cb_def_oil.setChecked(entity.def_oil)
        self.ui.cb_def_pot.setChecked(entity.def_pot)
        self.ui.sb_def_costume.setValue(entity.def_costume)
        self.ui.sb_def_pet.setValue(entity.def_pet)
        self.ui.sb_def_pet_pvp.setValue(entity.def_pet_pvp)
        self.ui.sb_def_pvp_hono.setValue(entity.def_pvp_hono)
        self.ui.sb_def_pvp_book.setValue(entity.def_pvp_book)

        # Element
        self.ui.sb_fairy.setValue(entity.fairy)
        self.ui.dropdown_element.setCurrentIndex(entity.type)
        self.ui.sb_res.setValue(entity.res)

        # Buffs
        self.ui.sb_morale_bonus.setValue(entity.morale_bonus)

    def guarantee_non_emptiness(self):
        if not self.entities:
            new_entity = Entity()
            self.entities.append(new_entity)
            self.ui.dropdown_entity.addItem(new_entity.name)
            self.display_editor_entity(0)
