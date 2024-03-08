from flask import Flask, request, jsonify
from flask_cors import CORS
from model.db import MODEL

app = Flask(__name__);
CORS(app)

@app.route("/rota", methods = ["POST"])
def index(): 
    return "oi"


@app.route("/rotadois", methods = ["GET"])
def rotadois(): 
    return "ola"


@app.route("/rayane/<variavel>", methods = ["GET"])
def rayane(variavel):    
    return "valor da variavel: " +variavel


@app.route("/santos/<variavel>/<var2>/<var3>", methods = ["GET"])
def santos(variavel, var2, var3):
    juntar = variavel+" "+var2+" "+var3    
    return "valor da variavel: " +juntar


@app.route("/list-user/<int:id>", methods = ["GET"])
def list_user(id):    
    return "id do usuario: " +str(id)


@app.route("/list/", methods = ["GET"])
def list():    
    return MODEL


@app.route("/list/name", methods = ["GET"])
def list_names():    
    list_names = []
    for names in MODEL:
        print(names['nome'])
        list_names.append(names['nome'])
    return list_names


@app.route("/test-request/", methods = ["GET","POST","DELETE","PUT"])
def test_request():
    if request.method == 'GET':
        print('method==GET')
    elif request.method == 'POST':
        print('method == POST')
    elif request.methos == 'DELETE':
        print('method == DELETE')
    else:
        print('method == PUT')
    return "a"


@app.route("/get-list/", methods = ["POST"])
def get_list():
    list = request.get_json()
    print(list)
    return 'a'




if __name__ == "__main__":
    app.run(debug=True)
    

