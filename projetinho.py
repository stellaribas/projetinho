from flask import Flask, render_template

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
