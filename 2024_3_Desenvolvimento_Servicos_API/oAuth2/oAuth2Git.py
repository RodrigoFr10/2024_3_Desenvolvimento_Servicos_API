import os
from flask import Flask, redirect, url_for, session, request
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(24)
#Ov23liTE4MkQovejJkOD
#64de889f17da6f204da317a1ba051e7fe5f21f3a
# Informações do Cliente (obtidas do GitHub Developer Console)
client_id = ''
client_secret = ''
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'
redirect_uri = 'http://localhost:5000/callback'

# Escopo para solicitar permissão para acessar o nome do usuário
scope = ['user']

@app.route('/')
def index():
    return 'Bem-vindo! <a href="/login">Login com GitHub</a>'

@app.route('/login')
def login():
    github = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = github.authorization_url(authorization_base_url)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    github = OAuth2Session(client_id, redirect_uri=redirect_uri, state=session['oauth_state'])
    github.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
    
    # Obter informações do usuário
    user_info = github.get('https://api.github.com/user').json()
    return f'Olá, {user_info["name"]}!'

if __name__ == '__main__':
    app.run(debug=True,port=5000)
