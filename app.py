# app.py
# Importa a classe Flask e a função render_template do pacote flask
from flask import Flask, render_template

# Cria uma instância da aplicação Flask
# __name__ é uma variável especial em Python que representa o nome do módulo atual.
# Flask a utiliza para saber onde procurar por recursos como templates e arquivos estáticos.
app = Flask(__name__)

# --- Rota Principal ---
# O decorador @app.route('/') define a URL raiz da sua aplicação.
# Quando alguém acessar "http://127.0.0.1:5000/", a função index() será executada.
@app.route('/')
def index():
    """
    Renderiza a página inicial (index.html).
    """
    # render_template procura por 'index.html' na pasta 'templates' e o envia para o navegador.
    return render_template('index.html')

# --- Rotas para as Apresentações ---

# Rota para a apresentação do Capítulo 1
@app.route('/apresentacao_capitulo_1.html')
def apresentacao_capitulo_1():
    """
    Renderiza a apresentação do Capítulo 1.
    """
    return render_template('apresentacao_capitulo_1.html')

# Rota para a apresentação do Capítulo 2
@app.route('/apresentacao_capitulo_2.html')
def apresentacao_capitulo_2():
    """
    Renderiza a apresentação do Capítulo 2.
    """
    return render_template('apresentacao_capitulo_2.html')

# Rota para os exercícios do Capítulo 2
@app.route('/exercicios_capitulo_2.html')
def exercicios_capitulo_2():
    """
    Renderiza os exercícios do Capítulo 2.
    """
    return render_template('exercicios_capitulo_2.html')

# Rota para a apresentação do Capítulo 3
@app.route('/apresentacao_capitulo_3.html')
def apresentacao_capitulo_3():
    """
    Renderiza a apresentação do Capítulo 3.
    """
    return render_template('apresentacao_capitulo_3.html')

# Rota para os exercícios do Capítulo 3
@app.route('/exercicios_capitulo_3.html')
def exercicios_capitulo_3():
    """
    Renderiza os exercícios do Capítulo 3.
    """
    return render_template('exercicios_capitulo_3.html')


# --- Execução da Aplicação ---
# A condição 'if __name__ == "__main__":' garante que o servidor de desenvolvimento
# só será iniciado quando o script for executado diretamente (e não quando for importado).
if __name__ == '__main__':
    # app.run() inicia o servidor web do Flask.
    # debug=True ativa o modo de depuração, que recarrega o servidor automaticamente
    # a cada alteração no código e mostra mensagens de erro detalhadas no navegador.
    app.run(debug=True)
