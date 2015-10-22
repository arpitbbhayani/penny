from app.items.todo import Todo
from app.dao.serviceDao.todoServiceDao import TodoServiceDao

def delete_todo(id):
    """
    Deletes a Todo with id = id
    """
    todoObj = Todo(None, None)
    todoObj.id = id

    r = TodoServiceDao().delete_todo(todoObj)
    return r is not None


def create_todo(name):
    """
    Creates a new Todo in the system with name = name and returns the Object
    """
    todoObj = Todo(name, '')
    id = TodoServiceDao().create_todo(todoObj)
    todoObj.id = id

    return todoObj


def save_todo(todoObj):
    """
    Updates the todoObj in database
    """
    r = TodoServiceDao().save_todo(todoObj)
    return r


def get_todos():
    """
    Returns the list of Todo Objects
    """
    todos = TodoServiceDao().get_all_todos()
    return [Todo.fromDB(todo) for todo in todos]
