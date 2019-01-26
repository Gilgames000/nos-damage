import sys

from PySide2 import QtWidgets

import util.persistence as ps
from controllers.calculator import CalculatorController
from controllers.editor import EditorController
from gui import Ui_MainWindow
from util.observables import ObservableList

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    entities = ObservableList(ps.load_entities())

    editor_controller = EditorController(ui, entities)
    calculator_controller = CalculatorController(ui, entities)

    entities.add_observer(calculator_controller)

    for i in entities:
        print(i)

    main_window.show()
    sys.exit(app.exec_())
