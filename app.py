from flask import Flask, jsonify, request, json
from methods import *

app = Flask(__name__)


@app.route('/dev', methods=['GET'])
def desenvolvedor():
    if request.method == 'GET':
        try:
            desenvolvedor = read()
            if desenvolvedor:
                return desenvolvedor
            else:
                return "Nenhum desenvolvedor cadastrado"
        except Exception as e:
            return "Error: {e}"


@app.route('/dev/<int:id>', methods=['GET'])
def dev_get(id: int):
    try:
        desenvolvedor = read()
        if not desenvolvedor:
            return "Nenhum desenvolvedor cadastrado"
        else:
            desenvolvedor = json.loads(desenvolvedor)
            desenvolvedor = [*desenvolvedor]
            return desenvolvedor[id]
    except Exception as e:
        return "Error: {e}"


@app.route('/dev/insert', methods=['POST'])
def dev_insert():
    try:
        dados = json.loads(request.data)
        updateList(dados)
        return "Success"
    except Exception as e:
        return "Error: {e}"


@app.route('/change/<int:id>', methods=['PUT'])
def dev_change(id: int):
    if request.method == "PUT":
        try:
            desenvolvedor = read()
            desenvolvedor = json.loads(desenvolvedor)
            desenvolvedor = [*desenvolvedor]
            dados = json.loads(request.data)
            desenvolvedor[id] = dados
            write(desenvolvedor)
            return jsonify(dados), 201
        except Exception as e:
            return "Error: {e}"


@app.route('/del/<int:id>', methods=["DELETE"])
def delete_dev(id: int):
    if request.method == "DELETE":
        try:
            desenvolvedor = read()
            desenvolvedor = json.loads(desenvolvedor)
            desenvolvedor = [*desenvolvedor]
            desenvolvedor.pop(id)
            write(desenvolvedor)
            return "Success", 201
        except Exception as error:
            return "Id não localizado"


if __name__ == "__main__":
    app.run(debug=True)