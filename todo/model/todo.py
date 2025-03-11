class Todo:
    def __init__(self, code_id: int, tilte: str, description: str):
        self.code_id: int = code_id
        self.title: str = tilte
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] =[]

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        print(f"{self.code_id}-{self.title}")

class TodoBook:

    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        generar_id = len(self.todos) + 1
        objeto_clase_Todo = Todo(title, description)
        self.todos[generar_id] = objeto_clase_Todo

    def pending_todos(self) -> list[Todo]:
        completados_falsos = [Todo.completed  for Todo in list(self.todos.values())]
