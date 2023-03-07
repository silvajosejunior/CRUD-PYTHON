from flask import Flask, render_template, request, redirect, url_for, flash
import urllib.request
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.sqlite3"

db = SQLAlchemy(app)

frutas = []
registros = []


class courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch


@app.route('/', methods=["GET", "POST"])
def function():
    # frutas = ['maça','uva','pera','abacaxi', 'ABACATE', 'banana', 'melao', 'tangerina','tucuma']

    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # notas = {'MARIO': 9.0, 'Marilia': 9.9, 'Maria': 8.0, 'joao':9.0}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)


@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    global url
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"
    elif propriedade == 'Kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"
    elif propriedade == 'Drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"
    elif propriedade == 'Tom_Cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"

    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])


@app.route('/courses')
def lista_courses():
    return render_template("courses.html", courses=courses.query.all())

@app.route('/cria_course', methods=["GET", "POST"])
def cria_course():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    ch = request.form.get('ch')

    if request.method == 'POST':
        if not nome or not descricao or not ch:
            flash("Preencha todos os campos do formulario", "error")
        else:
            course = courses(nome, descricao, ch)
            db.session.add(course)
            db.session.commit()
            return redirect(url_for('lista_courses'))
    return render_template("novo_course.html")


@app.route('/<int:id>/atualiza_course', methods=["GET", "POST"])
def atualiza_course(id):
    course = courses.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        ch = request.form["ch"]

        courses.query.filter_by(id=id).update({"nome": nome, "descricao": descricao, "ch": ch})
        db.session.commit()
        return redirect(url_for('lista_courses'))
    return render_template("atualiza_course.html", course=course)


@app.route('/<int:id>/remove_course')
def remove_course(id):
    course = courses.query.filter_by(id=id).first()
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('lista_courses'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
