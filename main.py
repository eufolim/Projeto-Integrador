from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify, send_file
import flask 
import os
import json
import requests
import time
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)

LOGIN_HTML = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        *{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body{
            font-family: 'Libre Franklin', sans-serif;
            background-image: url('https://static.vecteezy.com/ti/fotos-gratis/p1/6241112-moderno-preto-abstrato-gradiente-radial-fundo-tecnologia-design-corporativo-espaco-em-branco-para-texto-gratis-foto.jpg 2041w, https://static.vecteezy.com/ti/fotos-gratis/p2/6241112-moderno-preto-abstrato-gradiente-radial-fundo-tecnologia-design-corporativo-espaco-em-branco-para-texto-gratis-foto.jpg 4083w');
            background-size: cover; /* Certifica que a imagem cubra toda a página */
            background-attachment: fixed; /* Faz com que o fundo não se mova com o scroll */
        }

        h1 {
            font-weight: bold;
            margin: 0;
            margin-bottom: 1rem;
        }

        p {
            font-size: 14px;
            font-weight: 100;
            line-height: 20px;
            letter-spacing: 0.5px;
            margin: 20px 0 30px;
        }

        span {
            font-size: 12px;
        }

        a {
            color: #333;
            font-size: 14px;
            text-decoration: none;
            margin: 15px 0;
        }

        /* botão de sign in */
        .btn-grad {background-image: linear-gradient(to right, black 0%, gray  51%, black  100%)} 
        .btn-grad {
        margin: 10px;
        padding: 15px 45px;
        text-align: center;
        text-transform: uppercase;
        transition: 0.6s;
        background-size: 200% auto;
        color: white;            
        border-radius: 15px;
        border: none;
        display: block;
        cursor: pointer;
        }

        .btn-grad:hover {
            background-position: right center; 
            color: #fff;
            text-decoration: none;
        }

        #signIn{
            background-image: linear-gradient(to right, #fff 0%, #f7f3f3  51%, #fff  100%);
            color: #551cbe;
        }

        form {
            background-color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 0 50px;
            height: 100%;
            text-align: center;
        }

        input {
            background-color: #eee;
            border: none;
            border-radius: 15px;
            padding: 12px 15px;
            margin: 8px 0;
            width: 100%;
        }

        /*  */
        .login-container{
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;


        }
        .container {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.25), 0 5px 5px rgba(0, 0, 0, 0.22);
            position: relative;
            overflow: hidden;
            width: 768px;
            max-width: 100%;
            min-height: 480px;
        }

        img{
            margin-bottom: 30px;
        }

        .form-container {
            position: absolute;
            top: 0;
            height: 100%;
            transition: all 0.6s ease-in-out;
        }

        .sign-in-container {
            left: 0;
            width: 50%;
            z-index: 2;
        }


        .overlay-container {
            position: absolute;
            top: 0;
            left: 50%;
            width: 50%;
            height: 100%;
            overflow: hidden;
            transition: transform 0.6s ease-in-out;
            z-index: 100;
        }

        .overlay {
            background: #6441A5;
            background: -webkit-linear-gradient(to right, #6441A5, #2a0845);
            background: linear-gradient(to right, #6441A5, #2a0845);
            background-repeat: no-repeat;
            background-size: cover;
            background-position: 0 0;
            color: #ffffff;
            position: relative;
            left: -100%;
            height: 100%;
            width: 200%;
            transform: translateX(0);
            transition: transform 0.6s ease-in-out;
        }

        .error {
            color: #ff0000; 
            margin-top: 15px; 
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="container" id="container">
            <div class="form-container sign-in-container">
                <form method="post" action="/number_doc">
                    <img style="margin-bottom: 30px; margin-top: 10px;" width="240" height="130" src="https://logo-suggestion.renderforest.com/suggestions-images/0fb9/4167/0fb94167fa3ed65740dbe41f254e032d.png" class="attachment-medium size-medium img-fluid" alt="Logo Open Market" loading="lazy">
                    <input type="text" placeholder="Digite seu nome..." name="username" required />
                    <button type="submit" class="btn-grad" >Entrar</button> 
                </form> 
                {% if error %}
                    </br><p class="error">{{ error }}</p>
                {% endif %}
            </div>

            <div class="overlay-container"> 
                <div class="overlay">
                    <img style="margin-left: 180px;" src="https://i.ibb.co/Fsx0ZDq/image.png" width= "600" height: "200">  
                </div> 
            </div>
        </div> 
    </div>
</body>
</html> 
''' 


@app.route('/', methods=['GET'])
def login():
    return render_template_string(LOGIN_HTML)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)