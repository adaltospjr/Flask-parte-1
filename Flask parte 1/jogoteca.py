from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'games'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('adalto', 'Adalto Linhares', 'Sasuke')
usuario2 = Usuario('amanda', 'Amanda Melchiades', 'Neji')
usuario3 = Usuario('caie', 'Caie Linhares', 'caberça')


usuarios = {usuario1.id: usuario1, 
            usuario2.id: usuario2, 
            usuario3.id: usuario3 }


jogo1 = Jogo('AC Origins', 'RPG', 'Xbox One and Playstation 4')
jogo2 = Jogo('Halo', 'FPS', 'Xbox One')
jogo3 = Jogo('God of War', 'Ação', 'Playstation 4')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' Logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário ou senha inválidos.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] =  None
    flash('Nenhum usuário logado.')
    return redirect(url_for('index'))

#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)
