from flask import Flask, render_template, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


# Aqui são colocadas as rotas para cada página html

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
@app.route('/sala', methods=['POST'])
def sala():
    player_name = request.form.get('nome')
    room_code = request.form.get('codigo_sala')
    # Aqui você pode passar esses dados para o template ou processá-los como necessário
    return render_template('sala.html', player_name=player_name, room_code=room_code)

if __name__ == '__main__':
    app.run(debug=True)