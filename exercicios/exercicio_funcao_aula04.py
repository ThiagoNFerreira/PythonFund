numero = int(input('Digite um número: '))

def parImpar(numero):
    
    if numero % 2 == 0:
        print('É par')
    else:
        print('É impar')

parImpar(numero)

# Criar sistema de loja de roupas

# O sistema conterá as seguintes funções?

# verProduto -> lista com dicinários
    #{nome: Camiseta Hulk, tamanho: M, preco: 390}

# addProdutoCarrinho -> adiciona produto no carrinho

# addDesconto -> se utilizado no carrinho terá 20% de desconto

# removeProduto -> remove um produto do carrinho

# checkout -> mostra total da compra

# mainMenu -> Menu principal do sistema