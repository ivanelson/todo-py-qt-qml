import sqlite3
from models.task import Task

class TaskRepository:
    def __init__(self, db_path="tasks.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    task_name TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)

    def add(self, task: Task):
        with self.conn:
            self.conn.execute("""
                INSERT INTO tasks (title, task_name, created_at, status)
                VALUES (?, ?, ?, ?)
            """, (task.title, task.task_name, task.created_at, task.status))

    def update(self, task: Task):
        with self.conn:
            self.conn.execute("""
                UPDATE tasks
                SET title = ?, task_name = ?, status = ?
                WHERE id = ?
            """, (task.title, task.task_name, task.status, task.id))

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, task_name, created_at, status FROM tasks")
        rows = cursor.fetchall()
        return [Task(title, task_name, status, created_at, id) for id, title, task_name, created_at, status in rows]