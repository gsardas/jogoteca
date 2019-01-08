from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GRA')
jogo3 = Jogo('Mortal Kom', 'RPG', 'Xbox')
jogo4 = Jogo('Xadres', 'Tabuleiro', 'PC')
lista = [jogo1, jogo2, jogo3, jogo4]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)



