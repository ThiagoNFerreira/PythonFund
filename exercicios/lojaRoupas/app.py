from modules import produtos

def mainMenu():
    while True:
        print("Menu principal")
        print("1 - Sistema de produtos")
        print("2 - Caixa registradora")
        print("3 - Sair")

        opcao1 = int(input("Digite a opção: "))

        if opcao1 == 1:
            print("Menu de produtos")
            print("1 - Ver Produtos")
            print("2 - Adicionar Produto")
            print("3 - Remover Produto")
            print("4 - Sair")
            opcao2 = int(input(">>>>"))
            produtos.produtos
            if opcao2 == 1:
                produtos.verProdutos()
            elif opcao2 == 2:
                nome = input("Digite o nome do protudo: ")
                tamanho = input("Digite o tamanho: ")
                preco = float(input("Digite o preço: "))
                produtos.addProduto(nome, tamanho, preco)
            elif opcao2 == 3:
                nome = input("Digite o nome do produto a ser removido: ")
                produtos.removerProduto(nome)
            elif opcao2 == 4:
                continue
        elif opcao1 == 2:
            print("Caixa Registradora")
            print("1 - Ver Carrinho")
            print("2 - Adicionar produto ao carrinho")
            print("3 - Remover produto do carrinho")
            print("4 - Finalizar compra")
            print("5 - Sari")
            opcao3 = int(input(">>>>"))
            if opcao3 ==1:
                pass
            elif opcao3 == 2:
                for e, p in enumerate(produtos.produtos):
                    print("Produtos: ")
                    print(f"{e+1} - {p['nome']} - {p['preco']}")

        elif opcao1 == 2:
            pass
        elif opcao1 == 3:
            break
    
mainMenu()