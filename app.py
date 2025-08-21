from flask import Flask, render_template

app = Flask(__name__)

# Estrutura de navegação para os capítulos a ser passada para os templates
chapters = [
    {
        "title": "Capítulo 1: Motivação",
        "links": [
            {"text": "Apresentação", "endpoint": "apresentacao_capitulo_1"},
        ]
    },
    {
        "title": "Capítulo 2: Ambiente",
        "links": [
            {"text": "Apresentação", "endpoint": "apresentacao_capitulo_2"},
            {"text": "Exercícios", "endpoint": "exercicios_capitulo_2"},
        ]
    },
    {
        "title": "Capítulo 3: Variáveis",
        "links": [
            {"text": "Apresentação", "endpoint": "apresentacao_capitulo_3"},
            {"text": "Exercícios", "endpoint": "exercicios_capitulo_3"},
        ]
    }
]

# --- Rota Principal ---

@app.route('/')
def index():
    return render_template('index.html', chapters=chapters)

# --- Rotas para as Apresentações ---

# Rota para a apresentação do Capítulo 1
@app.route('/apresentacao_capitulo_1.html')
def apresentacao_capitulo_1():
    return render_template('apresentacao_capitulo_1.html', chapters=chapters)

# Rota para a apresentação do Capítulo 2
@app.route('/apresentacao_capitulo_2.html')
def apresentacao_capitulo_2():
    return render_template('apresentacao_capitulo_2.html', chapters=chapters)

# Rota para os exercícios do Capítulo 2
@app.route('/exercicios_capitulo_2.html')
def exercicios_capitulo_2():
    return render_template('exercicios_capitulo_2.html', chapters=chapters)

# Rota para a apresentação do Capítulo 3
@app.route('/apresentacao_capitulo_3.html')
def apresentacao_capitulo_3():
    return render_template('apresentacao_capitulo_3.html', chapters=chapters)

# Rota para os exercícios do Capítulo 3
@app.route('/exercicios_capitulo_3.html')
def exercicios_capitulo_3():
    return render_template('exercicios_capitulo_3.html', chapters=chapters)


# --- Execução da Aplicação ---

if __name__ == '__main__':
    app.run(debug=True)
