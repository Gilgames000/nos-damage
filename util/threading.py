from PySide2.QtCore import QRunnable


class Runnable(QRunnable):
    def __init__(self, func):
        super(Runnable, self).__init__()
        self.run = func
