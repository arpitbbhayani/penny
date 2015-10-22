from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from flask.ext.restful import reqparse

from app.items.todo import Todo
from app.dao.todoDao import TodoDao

from app.service import todosService

from bson import ObjectId

mod = Blueprint('todos', __name__, )

@mod.route('/create', methods=['POST'])
def create():
    todoObj = todosService.create_todo('Default Name')
    return jsonify(todoObj.jsonify())


@mod.route('/delete', methods=['POST'])
def delete():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=ObjectId, help='Rate cannot be converted', location='form')
    args = parser.parse_args()

    id = args.get('id')
    deleted = todosService.delete_todo(id)

    return jsonify(deleted = deleted)


@mod.route('/save', methods=["POST"])
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
