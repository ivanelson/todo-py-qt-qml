from PySide6.QtCore import QObject, Signal, Slot, Property
from services.task_service import TaskService

class TaskController(QObject):
    tasksChanged = Signal()
    errorOccurred = Signal(str)

    def __init__(self):
        super().__init__()
        self.service = TaskService()
        self._tasks_qt = ""

    @Slot(str, str, str)
    def addTask(self, title, task_name, status):
        success, error = self.service.add_task(title, task_name, status)
        if not success:
            self.errorOccurred.emit(error)
            return
        self._updateTasks()

    @Slot(int, str, str, str)
    def updateTask(self, id, title, task_name, status):
        success, error = self.service.update_task(id, title, task_name, status)
        if not success:
            self.errorOccurred.emit(error)
            return
        self._updateTasks()

    @Slot(str)
    def filterTasks(self, status):
        filtered = self.service.get_tasks_by_status(status)
        self._tasks_qt = "\n".join(
            f"[{t.status.upper()}] {t.title}: {t.task_name} ({t.created_at})"
            for t in filtered
        )
        self.tasksChanged.emit()

    @Slot(result='QVariantList')
    def getTaskList(self):
        task_list = self.service.get_all_tasks()
        return [
            {
                "id": t.id,
                "title": t.title,
                "task_name": t.task_name,
                "status": t.status,
                "created_at": t.created_at
            } for t in task_list
        ]

    def _updateTasks(self):
        tasks = self.service.get_all_tasks()
        self._tasks_qt = "\n".join(
            f"[{t.status.upper()}] {t.title}: {t.task_name} ({t.created_at})"
            for t in tasks
        )
        self.tasksChanged.emit()

    def getTasks(self):
        return self._tasks_qt

    tasks = Property(str, getTasks, notify=tasksChanged)