# Criar aplicação de calculo de média
nome = input("Nome aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print ("")

print ("-----------------------------------------------")

print ("Sr. ", nome, "Sua média foi ", media)

print ("-----------------------------------------------")

print ("Sr {}, sua média foi {}".format(nome,media))

print ("-----------------------------------------------")

print (f"Sr. {nome} Sua média foi {media}")

print ("-----------------------------------------------")

print ("")

if media >= 7:
    print(f"O aluno {nome} foi Aprovado")
    print("")

elif media >= 6:
    print(f"o aluno {nome} está de recuperação")
    print("")

else:
    print (f"O aluno {nome} foi reprovado")
    print("")
