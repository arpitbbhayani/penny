from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from flask.ext.restful import reqparse

from app.items.todo import Todo
from app.dao.todoDao import TodoDao

from app.service import todosService

from bson import ObjectId

mod = Blueprint('todo', __name__, )

@mod.route('/create', methods=['POST'])
def create():
    todoObj = todosService.create_todo('Default Name')
    return jsonify(todoObj.jsonify())

@mod.route('/save', methods=["POST"])
def save():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=ObjectId, help='Rate cannot be converted', location='form')
    parser.add_argument('mdcontent', required=True, type=unicode, help='mdcontent is not unicode', location='form')
    args = parser.parse_args()

    id = args.get('id')
    mdcontent = args.get('mdcontent')

    todoObj = Todo(id=id, c=mdcontent)

    dao = TodoDao(todoObj)
    ret = dao.save()
    return jsonify(id = str(id))


@mod.route('/getid', methods=["GET"])
def getid():
    dao = TodoDao(None)
    id = dao.getTodoId()
    return jsonify(id = str(id))


@mod.route('/get', methods=["GET"])
def getTodo():
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=ObjectId, help='Todo ID should be passed', location='args')
    args = parser.parse_args()

    todoObj = Todo.fromId(args.get('id'))
    return jsonify(id=str(todoObj.getId()), content=todoObj.getContent())
