produtos = []

def addProduto(nome, tamanho, preco):
    produto = {
        'nome': nome,
        'tamanho': tamanho,
        'preco': preco
    }
    
    produtos.append(produto)

def verProduto():
    for p in produtos:
        print('================')
        print(f"Nome: {p['nome']}")
        print(f"Tamanho: {p['tamanho']}")
        print(f"Preço: {'preco'}") 

def removerProduto(produto):
    for p in produtos:
        if p==['Nome'] == produto:
            produtos.remove(p)
