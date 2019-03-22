# app.py
from flask import Flask, request, jsonify  # import flask

from Service import ToDoService
from models import Schema

# import json

app = Flask(__name__)             # create an app instance

@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())

@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))

@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return ToDoService().update(item_id, request.get_json())

@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return ToDoService().delete(item_id)

if __name__ == "__main__":         # on running python app.py
    Schema()
    app.run(debug = True)                     # run the flask app