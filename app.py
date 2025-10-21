from flask import Flask

app = Flask(__name__)

lista_produtos = ['Caneta Azul', 'Tesoura', 'Caderno', 'Fichario', 'Cola Branca', 'Borracha']

# Home
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>Produtos Papelaria</h1>
    <p>URLs:<p>
    <p>Create: /create/string:produto</p>
    <p>Read: /read</p>
    <p>Update: /update/int:indice/string:produto</p>
    <p>delete: /delete/int:indice</p>
    """

# Create
@app.route('/create/<string:produto>', methods=['GET'])
def create_produto(produto):
    lista_produtos.append(produto)
    return 'O produto ' + produto + ' foi adicionado com sucesso.'

# Read
@app.route('/read', methods=['GET'])
def read_produtos():
    return lista_produtos

# Update
@app.route('/update/<int:indice>/<string:produto>', methods=['GET'])
def update_produto(indice, produto):
    lista_produtos[indice] = produto
    return 'Produto atualizado com sucesso.'

# Delete
@app.route('/delete/<int:indice>', methods=['GET'])
def delete_produto(indice):
    armazena_produto = lista_produtos[indice] 
    lista_produtos.pop(indice)
    return 'O produto ' + armazena_produto + ' foi deletado com sucesso.'

if __name__ == '__main__':
    app.run(debug=True)