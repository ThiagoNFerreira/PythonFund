# Criar uma aplicação que consuma a api do viacep

# Funções:
    # IformaRua - recebe um cep e informa a rua
    # InformaBairro - recebe um cep e informa o bairro
    # Consultar CEP Full - recebe o cep e informa o endereço completo

import json
import requests
#from typing import Text


def main():
    while True:
        infCEP = input("Informe um CEP: ")
        consulta = consultaCEP(infCEP)
        print('1 - Consultar Tudo')
        print('2 - Consultar Bairro')
        print('3 - Consultar Rua')
        print('4 - Sair')
        opcao = input('>>>>')

        if opcao == '1':
            print(consulta)
        elif opcao == '2':
            print(consulta['lograduro'])
        elif opcao == '3':
            print(consulta['bairro'])
        elif opcao == '4':
            break
        else:
            print('Busca Inválida')


def consultaCEP(cep):
    viacep = f'https://viacep.com.br/ws/{cep}/json'
    req = requests.get(viacep).text
    return req



main()





    
    # with open('arquivo.json', 'r') as arquivo:
    #     conteudo = arquivo.readlines()
    #     for linha in conteudo:
    #         if cpf in linha.split('\t'):
    #             registro = linha.split('\t')
    #             print('CPF', registro[0])
    #             print('Nome', registro[1])
    #             print('Idade', registro[2])
    #             print('Sexo', registro[3])
    #             print('Nacinalidade', registro[4])
    #             input('Digite enter para voltar ao menu principal')
    #         else:
    #             print('Registro não encontrado')