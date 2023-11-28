# primeira api com Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# 1 -  Definir o objetivo da API:
'''Criar uma API de blog, com as funções: Consultar, Postar, Editar, Excluir postagens '''

postagens = [
    {
        'titulo': 'Minha história',
        'autor': 'Amanda Dias'
    },

    {
        'titulo': 'Novo dispositivo Sony',
        'autor': 'Howard Stringer'
    },

    {
        'titulo': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]

# rota padrão - GET http://localhist:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET http://localhist:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagens_por_indice(indice):
    return jsonify(postagens[indice])

# Criar nova postagem - POST http://localhist:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Alterar uma postagem - PUT http://localhist:5000/postagem/id
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE http://localhist:5000/postagem/id
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    if postagens[indice] is not None:
        del postagens[indice]
        return jsonify(f'Foi excluido a postagem {postagens[indice]}', 200)
    return jsonify('Não foi possível encontrar a postagem para exclusão', 404)


app.run(port=5000, host='localhost', debug=True)


# 2 - Definir a URL base da API:
'''ex: devaprender.com/api/ '''

# 3 - Definir os endpoints:
'''
> /postagens
> /consultas
> /edicao
> /exclusao

'''

# 4 - Quais recursos será disponibilizado pela API?
# exe: informações sobre as postagens

# 5 - Quais verbos http serão disponibilizados?
'''
- GET
- POST
- PUT
- DELETE
'''

# 6 - Quais são os URLs completos para cada um? (rota)
'''
    * GET http://localhost:5000/postagens
    * GET id http://localhost:5000/postagens/1
    * POST id http://localhost:5000/postagens
    * PUT id http://localhost:5000/postagens/1
    * DELETE id http://localhost:5000/postagens/1
'''
  

    