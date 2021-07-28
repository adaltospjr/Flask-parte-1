from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('AC Origins', 'RPG', 'Xbox One and Playstation 4')
    jogo2 = Jogo('Halo', 'FPS', 'Xbox One')
    jogo3 = Jogo('God of War', 'Ação', 'Playstation 4')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

#app.run(host='0.0.0.0', port=8080)
app.run()
