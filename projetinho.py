from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('_Paginas/Cadastro.html')

@app.route('/Denuncias')
def Denuncias():
    return render_template('_Paginas/Denuncias.html')

@app.route('/Login')
def Login():
    return render_template('_Paginas/Login.html')

@app.route('/Mapa')
def Mapa():
    return render_template('_Paginas/Mapa.html')

@app.route('/QuemSomos')
def QuemSomos():
    return render_template('_Paginas/QuemSomos.html')

@app.route('/Curiosidades')
def Curiosidades():
    return render_template('_Paginas/Curiosidades.html')

if(__name__=='__main__'):
    app.run(debug=True)




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.bd'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.Usuario #poderia ser email...
