from datetime import datetime

class Task:
    STATUS_OPTIONS = {"novo", "em andamento", "cancelada", "concluida"}

    def __init__(self, title, task_name, status="novo", created_at=None, id=None):
        self.id = id
        self.title = title.strip()
        self.task_name = task_name.strip()
        self.status = status.strip().lower()
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._validate()

    def _validate(self):
        if not self.title:
            raise ValueError("Título é obrigatório.")
        if not self.task_name:
            raise ValueError("Nome da tarefa é obrigatório.")
        if self.status not in self.STATUS_OPTIONS:
            raise ValueError(f"Status inválido. Opções válidas: {self.STATUS_OPTIONS}")