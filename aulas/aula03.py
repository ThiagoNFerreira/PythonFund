## Regras da linguagem

# Palavras reservadas não podem ser utilizadas para nomear outras coisas.
# Estruturas de condições, repetições, funções, classes e contextos
# Comandos dentro de estruturas são identadas com 4 espaços
# Objetos criados não podem começar com números, vírgula, ponto...

## Estrutura de repetição

# While

# contador = 0

# while contador <= 100:
#     print(contador)
#     contador += 1

while True:
    print("Sistema de escolha")
    print("")
    print("1 - escolha primeira opção")
    print("2 - escolha segunda opção")
    print("0 - para sair")
    print("")

    opcao = int(input(">>> "))

    if opcao == 1:
        print("")
        print ("Você escolheu a primeira opção")
        print("")
    elif opcao == 2:
        print("")
        print ("Você escolheu a segunda opção")
        print("")
    elif opcao == 0:
        break
    else:
        print("")
        print("Opção inválida!")
    print("")

    # continue #função de controle do while, continue volta para o início do while
    # break # função de controle do while, para a repetição do while


# For

