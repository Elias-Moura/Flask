from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    def __str__(self):
        return f'{self.nome}'


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GTA V', 'Mundo aberto', 'Xbox 360/PS3')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html',titulo='Jogos', jogos=jogos)


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_gerado = Jogo(nome, categoria, console)
    jogos.append(jogo_gerado)
    return redirect('/')


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

app.run(debug=True)
