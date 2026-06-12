from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    nome_usuario = "Anna"
    idade_usuario = 17
    return render_template("index.html" , usuario = nome_usuario)

@app.route("/index2")
def index2():
    nome_usuario = "Becca"
    idade_usuario = 16
    return render_template("index2.html" , usuario = nome_usuario)

if __name__ == "__main__":
    app.run(debug= True)