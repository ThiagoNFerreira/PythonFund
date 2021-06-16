# # String - Conjunto de caracteres

# # Métodos de string

# nome = input ("Qual é seu nome: ")

# texto = "ola {}".format(nome)

# dividindoTexto = texto.split('a')
# caixaBaixa = texto.lower()
# caixaAlta = texto.upper()

# print(caixaAlta)
# print(caixaBaixa)
# print(dividindoTexto)

## Indexação de String

# texto2 = "Apenas uma string"
# print(texto2[4])
# print(texto2[6:]) #pega do sétimo elemento em diante
# print(texto2[:6]) #pega do sétimo elemento para trás
# print(texto2[5:10])#pega do intervalo definido, no caso do sexto ao décimo
# print(texto2[::2]) #pega de 2 em 2

# len(texto)

# Estrutura Condicional

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
habilitacao = input("Possui habilitação? s/n")
credito = True

if idade and>=18 and habilitacao == 's' and credito == True:
    print(f"Bem vindo {nome}")
    print("Você pode alugar um carro")

elif idade and>=18 and habilitacao == 's'
    print(f"Bem vindo {nome}")
    print("Você pode alugar um carro com pagamento adiantado")

else:
    print(f"Bem vindo {nome}")
    print("Rejected")