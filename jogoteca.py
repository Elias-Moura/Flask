from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)


class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return f'{self.nome}'

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Elias Moura', 'Elias', '1234')
usuario2 = Usuario('Marcelo', 'Botafogo', '5678')

usuarios_dict = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2, 
}



jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GTA V', 'Mundo aberto', 'Xbox 360/PS3')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_gerado = Jogo(nome, categoria, console)
    jogos.append(jogo_gerado)
    return redirect(url_for('index'))


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # '/login?proxima=novo'
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios_dict:
        usuario = usuarios_dict[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f'{usuario.nickname} logado com sucesso.')
            if request.form['proxima'] != 'None':
                proxima_pagina = request.form['proxima']
            else:
                proxima_pagina = url_for('index')
            
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))


app.run(debug=True)
