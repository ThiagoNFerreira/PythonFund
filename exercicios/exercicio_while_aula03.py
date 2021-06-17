nome = input("Insina seu nome: ")
idade = int(input("Insira sua idade: "))
email = input("Informe seu e-mail: ")
telefone = input("Informe seu telefone: ")

while True:
    print ("Bem vindo ", nome, " escolha uma das opções")
    print ("1 - Mostrar todas as informações")
    print ("2 - Mostrar nome e idade")
    print ("3 - Mostrar e-mail e telefone")
    print ("0 - Sair")

    opcao = int(input(">>> "))

    if opcao == 1:
        print (f"Seu nome é {nome}\nSua idade é {idade} \nSeu e-mail é {email} \nSeu telefone é {telefone}")
        break
    elif opcao == 2:
        print (f"Seu nome é {nome}\nSua idade é {idade}.")
        break
    elif opcao == 3:
        print (f"Seu e-mail é {email}\nSeu telefone é {telefone}.")
        break
    elif opcao == 0:
        break
    else:
        continue
