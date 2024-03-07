from flask import Flask

app = Flask(__name__);

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

if __name__ == "__main__":
    app.run(debug=True)
    

