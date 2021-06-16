# Criar aplicação de calculo de média
nome = input("Nome aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print ("Sr. ", nome, "Sua média foi ", media)

print ("Sr {}, sua média foi {}".format(nome,media))

print (f"Sr. {nome} Sua média foi {media}")
