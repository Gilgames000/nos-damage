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
    ui.sb_level.setValue(entity.level)
    ui.dropdown_element.setCurrentIndex(entity.type)
    print(entity.type, Element(entity.type))


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

    ui.dropdown_entity.currentIndexChanged.connect(display_editor_entity)

    display_editor_entity(0)

    for i in entities:
        print(i)

    main_window.show()
    sys.exit(app.exec_())
