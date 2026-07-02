from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def q1():
    nome_usuario = "Bianca"
    return render_template("q1.html", usuario = nome_usuario)

@app.route("/num2")
def q2():
    nome_usuario = "Rebecca"
    idade = 16  
    return render_template("q2.html", nome = nome_usuario, idade = idade )

@app.route("/num3")
def q3():
    usuario = {"nome": "Ana", "email": "ana@email.com"}
    return render_template("q3.html", dados = usuario)

@app.route("/num4")
def q4():
    usuarios = ["Ana", "Bianca", "Rebecca", "Manu", "Gabi"]
    return render_template("q4.html", dados = usuarios)

if __name__ == "__main__":
    app.run(debug=True)