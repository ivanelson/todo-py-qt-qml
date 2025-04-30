from models.task import Task
from repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def add_task(self, title, task_name, status="novo", created_at=None):
        try:
            task = Task(title, task_name, status, created_at)
        except ValueError as e:
            return False, str(e)
        self.repo.add(task)
        return True, None

    def update_task(self, id, title, task_name, status):
        try:
            task = Task(title, task_name, status, id=id)
            self.repo.update(task)
            return True, None
        except ValueError as e:
            return False, str(e)

    def get_all_tasks(self):
        return self.repo.get_all()

    def get_tasks_by_status(self, status=None):
        tasks = self.repo.get_all()
        if status and status.strip():
            status = status.strip().lower()
            return [t for t in tasks if t.status == status]
        return tasks