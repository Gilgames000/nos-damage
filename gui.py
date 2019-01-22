import sys

from PySide2 import QtWidgets
from datastructs.constants import Element
from datastructs.constants import MobType

from gui import Ui_MainWindow
import util.persistence as ps
from glob import glob


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
    ui.le_name.setText(entity.name)
    ui.dropdown_element.setCurrentIndex(entity.type)
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    entity_filenames = glob("entities/*.json")
    entities = [ps.load_entity(filename=fn) for fn in entity_filenames]

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
