from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'games'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

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
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' Logou com sucesso!')
        return redirect('/')
    else:
        flash('Usuário ou senha inválidos.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] =  None
    flash('Nenhum usuário logado.')
    return redirect('/login')

#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)