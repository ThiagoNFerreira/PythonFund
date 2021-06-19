## As 4 maneiras de trabalhar com funções

# 1 - Utilizando as funções built-in

# print()
# input()

# 2 - Importando apartir de módulos

# import os

# os.system("ls -lha")

# 3 - Criando suas próprias funções

# def soma(x,y):
#   returno x + y

# 4 - Utilizando funções anônimas

# soma = lambda x, y: x + y
# soma(10, 10)

# Escopo



# Parâmetros não obrigatórios (Definindo valor padrão para um parâmetro, não é necessário especificá-lo)

# def multiplica(x, y, z=1):
#     return x * y * z

# print (multiplica(10, 15))


# Parâmetros com palavra-chave (Ao colocar * como parâmetro, voce obriga o usuário digitar os parâmetros)

# def calculaPosicao(*, latitude, longetude):
#     posicao = latitude - longetude
#     return posicao

# calculaPosicao(latitude=14444454, longetude=4466466)

# Multiplos argumentos

# Args (ao colocar *junto ao parâmetro, por exemplo *nome, significa que você pode colocar inúmeros parâmetros)

# def soma(*num):
#     total = 0
#     for i in num:
#         total += i
#     print (total)

# soma(1, 2, 3, 4, 5)

# Multiplos argumentos com palavras-chaves

# KWargs

# def checkout(**valores):
#     total = 0 
#     for valor in valores.values():
#         print(valor)

# checkout(produto="camiseta", preco=150)