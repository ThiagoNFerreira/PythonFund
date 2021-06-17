cesta =[]

while True:
    
    print('Quitanda: ')
    print('1 - Ver cesta')
    print('2 - Adicionar fruta')
    print('3 - Sair')

    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        print(cesta)
    elif opcao == 2:
        print('Menu de frutas')
        print('1 - Banana')
        print('2 - Caju')
        print('3 - Manga')
        print('4 - Abacaxi')

        fruta = int(input('A digite a opção: '))
        
        if fruta == 1:
            cesta.append('Banana')
        elif fruta == 2:
            cesta.append('Caju')
        elif fruta == 3:
            cesta.append('Manga')
        elif fruta == 4:
            cesta.append('Abacaxi')
        else:
            print ('Opção inválida!')
    
    if opcao == 3:
        break

