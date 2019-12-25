import json
from os import path


def write(msg):
    try:
        with open('./dados.json', 'w') as file:
            json.dump(msg, file)
    except Exception as e:
        return f"Erro: {e}"


def read():
    if not path.isfile("dados.json"):
        write(dict)
    try:
        with open('./dados.json', 'r') as file:
            message = file.read()
            return message
    except Exception as e:
        return f"Erro: {e}"


def updateList(msg):
    file = read()
    lista = []
    if not file:
        lista.append(msg)
    else:
        file = json.loads(file)
        if file:
            lista = [*file]
        lista.append(msg)
    write(lista)
