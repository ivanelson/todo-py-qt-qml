import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from controllers.task_controller import TaskController

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

controller = TaskController()
engine.rootContext().setContextProperty("taskController", controller)

engine.load("ui/main.qml")
if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec())