from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')

@app.route("/")
def homepage():
    return render_template("inicio.html")

@app.route("/pergunta")
def pergunta():
    return render_template("pergunta.html")

@app.route("/pergunta2")
def pergunta2():
    return render_template("pergunta2.html")

@app.route("/errou")
def error():
    return render_template("error.html")

@app.route("/ultimapergunta")
def ultima():
    return render_template("ultima.html")

@app.route("/venceu'-'")
def ganhou():
    return render_template("ganhou.html")


if __name__ == "__main__":
    app.run(debug=True)
