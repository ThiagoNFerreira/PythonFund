cesta = []
total = 0

while True:
    print('Quitanda:')
    print('1 - ver cesta')
    print('2 - Adicionar fruta')
    print('3 - checkout')
    print('4 - Sair')
    opcao = int(input('Digite a Opção: '))
    if opcao == 1:
        for item in cesta:
            print(f"Produto: {item['nome']}, Valor: {item['valor']}")
    elif opcao == 2:
        print('Menu de frutas:')
        print('1 - Banana')
        print('2 - Caju')
        print('3 - Manga')
        print('4 - Abacaxi')
        banana = {'nome':'banana', 'valor': 1.50}
        caju = {'nome':'caju', 'valor': 4.50}
        manga = {'nome':'manga', 'valor': 2.50}
        abacaxi = {'nome':'abacaxi', 'valor': 5.00}
        fruta = int(input('Digite a Opção: '))
        if fruta == 1:
            cesta.append(banana)
        elif fruta == 2:
            cesta.append(caju)
        elif fruta == 3:
            cesta.append(manga)
        elif fruta == 4:
            cesta.append(abacaxi)
        else:
            print('Opção invalida')
    elif opcao == 3:
        print('Checkout')
        for item in cesta:
            total += item['valor']
        print(f'Total da Compra: {total}')
        break

        # print(f'Valor total: {}')

    elif opcao == 4:
        break
