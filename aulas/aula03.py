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

# while True:
#     print("Sistema de escolha")
#     print("")
#     print("1 - escolha primeira opção")
#     print("2 - escolha segunda opção")
#     print("0 - para sair")
#     print("")

#     opcao = int(input(">>> "))

#     if opcao == 1:
#         print("")
#         print ("Você escolheu a primeira opção")
#         print("")
#     elif opcao == 2:
#         print("")
#         print ("Você escolheu a segunda opção")
#         print("")
#     elif opcao == 0:
#         break
#     else:
#         print("")
#         print("Opção inválida!")
#     print("")

    # continue #função de controle do while, continue volta para o início do while
    # break # função de controle do while, para a repetição do while


# For

# texto = 'Olá, eu sou um texto'

# for caracter in texto:
#     print(f'agora a variável caracter é {caracter}')

produtos = ['Camiseta A', 'Camiseta B', 'Camiseta C', 'Calca 1']

for prod in produtos:
     print(prod)

## Conjuntos - Coleções 

# Listas - Conjunto de objetos

# Métodos de lista

# lista = ["String1", "string2", 2, 5, 5.6, True]
# lista.count(2) # realiza a contagem do que for informad entre parênteses
# lista.append("texto") # adiciona ao final da lista
# lista.insert(1,'info02') # especifica onde incluir o ítem na lista
# lista.remove("String2") #remove o ítem da lista com base no nome
# lista.pop(0) #remove o ítem da lista com base no índice.
# lista.clear() # limpa a lista

# Indexação de listas

# lista[0]
# lista[1][2][3][4]

# Tuplas é como se fosse uma lista imutável

# cadastro = ('Joao', 'Nascimento', 30)

# Dicionários é passado por chave e valor entre chaves

# dados_pessoais = {"Nome": "João", 
#                   "Idade": 36, 
#                   "Telefone": "444444444", 
#                   "Email": "teste@teste.com"}

# dados_estaduais = {
#     "SP" : {
#         "Nome": "São Paulo",
#         "População": 12000000,
#         "IDH": 15
#     },
#     "BH" : {
#         "Nome": "São Paulo",
#         "População": 2000000,
#         "IDH": 15
#     },
#     "RJ" : {
#         "Nome": "Rio de Janeiro",
#         "População": 6000000,
#         "IDH": 15
#     },
# }

# # Métodos de dict

# dados_pessoais.keys() # mostra as chaves
# dados_pessoais.values() # mostra os valores
# dados_pessoais.get() # não mostra warning e dá sequência no código sem quebrar
# dados_pessoais.clear() # limpa o dicionário

# Sets - não permite valores duplicados, definidos por chaves. Conjunto de valores únicos

#set(lista)
#conjunto = {1, 2, 3, 4, 5, 5, 5,} # mesmo criando um set com valores repetidos serão mostrados apenas os 1 valor de cara.