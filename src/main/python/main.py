import sys

from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox
from fbs_runtime.application_context import ApplicationContext

import util.persistence as ps
from controllers.calculator import CalculatorController
from controllers.editor import EditorController
from gui import Ui_MainWindow
from util.observables import ObservableList
from util.versiontools import VersionCheckerService


class AppContext(ApplicationContext):  # 1. Subclass ApplicationContext
    def show_update_dialog(self):
        title = "NosDamage update"
        message = (
            "A new version is available. "
            "Do you want to open the download page?"
        )
        buttons = QMessageBox.Yes | QMessageBox.No

        reply = QMessageBox.question(self.ui, title, message, buttons)

        if reply == QMessageBox.Yes:
            import webbrowser
            url = "https://github.com/Gilgames000/nos-damage/releases"
            webbrowser.open(url)

    def run(self):  # 2. Implement run()
        window = QMainWindow()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(window)
        version = self.build_settings['version']
        window.setWindowTitle("NosDamage v" + version)
        window.resize(250, 150)
        window.show()

        version_checker = VersionCheckerService(version)
        version_checker.needUpdate.connect(
            lambda need_update: (
                self.show_update_dialog()
                if need_update
                else None
            )
        )
        version_checker.start()

        entities = ObservableList(ps.load_entities())

        self.editor_controller = EditorController(self.ui, entities)
        self.calculator_controller = CalculatorController(self.ui, entities)

        entities.add_observer(self.calculator_controller)

        return self.app.exec_()  # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
