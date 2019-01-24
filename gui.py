import sys

from PySide2 import QtWidgets

import util.persistence as ps
from controllers.editor import EditorController
from gui import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    entities = ps.load_entities()

    editor_controller = EditorController(ui, entities)

    for i in entities:
        print(i)

    main_window.show()
    sys.exit(app.exec_())
