from flask import Flask

app = Flask(__name__);

@app.route("/rota", methods = ["POST"])
def index(): 
    return "oi"

@app.route("/rotadois", methods = ["GET"])
def rotadois(): 
    return "ola"

if __name__ == "__main__":
    app.run(debug=True)