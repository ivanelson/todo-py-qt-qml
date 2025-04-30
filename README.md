# 📝 ToDo App - Python + Qt + QML

Aplicação simples de cadastro e gerenciamento de tarefas, desenvolvida com **Python**, **Qt (QML)** e **SQLite**, seguindo uma arquitetura em camadas.

## 📦 Funcionalidades

- ✅ Cadastro de tarefas com título, descrição, status e data de criação.
- ✏️ Edição de tarefas existentes.
- 🔍 Filtro por status: `novo`, `em andamento`, `cancelada`, `concluida`.
- ⚠️ Validação visual de campos obrigatórios com borda vermelha.
- 💾 Persistência em banco de dados SQLite (`tasks.db`).
- 🧱 Arquitetura limpa e separada em camadas (Model, Service, Controller, View).

## 📁 Estrutura do Projeto

```
todo-app-python-qt-qml/
├── main.py
├── ui/
│   └── main.qml
├── controllers/
│   └── task_controller.py
├── models/
│   └── task.py
├── services/
│   └── task_service.py
├── repositories/
│   └── task_repository.py
├── tasks.db
├── requirements.txt (opcional)
├── README.md
```

## 🚀 Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/todo-app-python-qt-qml.git
cd todo-app-python-qt-qml
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale o PySide6:

```bash
pip install PySide6
```

4. Execute o projeto:

```bash
python main.py
```

## 🧠 Tecnologias

- Python 3.8+
- Qt/QML (via PySide6)
- SQLite

## 📌 Observações

- O banco de dados será criado automaticamente na primeira execução.
- O ID da tarefa é usado internamente para edição.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

---

Feito com ❤️ por Ivanelson Nunes
