import os

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pagina_inicial.html')

@app.route('/historico')
def historico():
    return render_template('pagina_historico.html')



@app.route('/erro')
def erro():
    return "Usuário já existente"



@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome-usuario']
        email = request.form['email-usuario']
        senha = request.form['senha-usuario']

        if os.path.exists(nome + ".txt"):
            return redirect(url_for('erro'))
        else: 
            arquivo_usuario = open(nome + ".txt", "a")
            arquivo_usuario.write(nome + "\n")
            arquivo_usuario.write(email + "\n")
            arquivo_usuario.write(senha + "\n")

        arquivo_usuario = open(nome + ".txt", "r")
        arquivo_usuario_read = arquivo_usuario.readlines()
        print(arquivo_usuario_read[0] == nome + "\n")
        return render_template('pagina_login.html')
            
        

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome-usuario']
        senha = request.form['senha-usuario']

        arquivo_usuario = open(nome +".txt", "r")
        arquivo_usuario2 = arquivo_usuario.readlines()

        if nome + "\n" == arquivo_usuario2[0] and senha + "\n" == arquivo_usuario2[2]:
            return  redirect(url_for('historico'))
        else:
            return "Usuário ou senha incorretos, tente novamente"
    else:
        return render_template('pagina_login.html')

app.run(debug=True)