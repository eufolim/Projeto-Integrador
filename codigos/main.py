from flask import Flask, render_template, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


# Aqui são colocadas as rotas para cada página html

@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/sala', methods=['POST'])
def sala():
    return "sala fazer html"

if __name__ == '__main__':
    app.run(debug=True)