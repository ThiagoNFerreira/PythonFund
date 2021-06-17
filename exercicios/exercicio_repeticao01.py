while True:
    
    geracao = int(input('Informe o ano de seu nascimento: '))

    if geracao <= 1964:
        print(f'Ano de nascimento é {geracao}: Geração Baby Boomer')
    elif geracao > 1964 and geracao <= 1979:
        print(f'Ano de nascimento é {geracao}: Geração X')
    elif geracao > 1979 and geracao <= 1994:
        print(f'Ano de nascimento é {geracao}: Geração Y')
    else:
        print(f'Ano de nascimento é {geracao}: Geração Z')
    