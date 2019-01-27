import sys

from PySide2.QtWidgets import QMainWindow
from fbs_runtime.application_context import ApplicationContext

import util.persistence as ps
from controllers.calculator import CalculatorController
from controllers.editor import EditorController
from gui import Ui_MainWindow
from util.observables import ObservableList


class AppContext(ApplicationContext):  # 1. Subclass ApplicationContext
    def run(self):  # 2. Implement run()
        window = QMainWindow()
        ui = Ui_MainWindow()

        ui.setupUi(window)
        version = self.build_settings['version']
        window.setWindowTitle("NosDamage v" + version)
        window.resize(250, 150)
        window.show()

        entities = ObservableList(ps.load_entities())

        self.editor_controller = EditorController(ui, entities)
        self.calculator_controller = CalculatorController(ui, entities)

        entities.add_observer(self.calculator_controller)

        return self.app.exec_()  # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
