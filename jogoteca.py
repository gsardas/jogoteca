from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
    jogo2 = Jogo('Pokemon', 'RPG', 'GRA')
    jogo3 = Jogo('Mortal Kom', 'RPG', 'GBA')
    jogo4 = Jogo('Xadres', 'Tabuleiro', 'PC')
    lista = [jogo1, jogo2, jogo3, jogo4]
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)

app.run()

