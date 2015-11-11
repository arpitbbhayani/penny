from flask import Blueprint
from flask import render_template, jsonify

from flask.ext.restful import reqparse
from flask.ext.login import login_required

from app.items.todo import Todo
from app.dao.todoDao import TodoDao

from app.service import todosService

from bson import ObjectId

mod = Blueprint('todos', __name__, )

@mod.route('/', methods=["GET"])
@login_required
def index():
    todos = todosService.get_todos()
    return render_template('pages/todo_widget.html', todos=todos)


@mod.route('/create', methods=['POST'])
@login_required
def create():
    todoObj = todosService.create_todo('Default Name')
    return jsonify(todoObj.jsonify())


@mod.route('/delete', methods=['POST'])
@login_required
def delete():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=ObjectId, help='Rate cannot be converted', location='form')
    args = parser.parse_args()

    id = args.get('id')
    deleted = todosService.delete_todo(id)

    return jsonify(deleted = deleted)


@mod.route('/save', methods=["POST"])
@login_required
def save():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=ObjectId, help='Rate cannot be converted', location='form')
    parser.add_argument('name', required=True, type=unicode, help='name is not unicode', location='form')
    parser.add_argument('content', required=True, type=unicode, help='content is not unicode', location='form')
    args = parser.parse_args()

    id = args.get('id')
    name = args.get('name')
    content = args.get('content')

    todoObj = Todo(name=name, content=content)
    todoObj.id = id

    updated = todosService.save_todo(todoObj)

    return jsonify(updated = updated)
