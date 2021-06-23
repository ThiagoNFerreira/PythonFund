##### CSV

# import csv

# with open("/home/developer/Python_Fundamentals/aulas/texto.csv", "r") as arquivo:
#     conteudo = csv.reader(arquivo,delimiter='.')
#     cabecalho = next(conteudo)
#     informacao01 = next(conteudo)
#     restante_info = []
#     next(conteudo)
#     for linha in conteudo:
#         restante_info.append(linha)


# print(cabecalho)
# print(informacao01)

# print(restante_info)

### JSON

import json
from typing import Text
# import requests

# cep = input("Informe o CEP: ")

# viacep = f'https://viacep.com.br/ws/{cep}/json'

# requisicao = requests.get(viacep)
# conteudo = requisicao.content

# with open('arquivo.json', 'wb') as jsonfile:
#     jsonfile.write(conteudo)

# file = open('registro.txt')
# jsonfile = json.load(file)
# print(jsonfile)

# from defusedxml import ElementTree as ET

# # Carregando Arquivo
# arquivo_xml = ET.parse('arquivo.xml')

# # Acessando primeira tag (tag root)
# root = arquivo_xml.getroot()

# # Iterando por todas as tags da tag root
# for elemento in root:
#     print(elemento.tag, elemento.text)

# print("======================")

# # Iterando sub tags
# for time in root.find("times"):
#     print(time.tag, time.attrib)

# print("======================")

# for time in root.find("times"):
#     print(time.tag, time.attrib)
#     for jogador in time:
#         print(f'Jogador: {jogador.text}\nQuantidade de gols: 1')

# print("======================")

from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

# Estrutura raiz do xml

raiz = Element('cadastro')

# Adicionar comentário ao xml

raiz.append(Comment("Cadastro de usuário da locadora xpto"))

# Adicionar elementos à árvore:

# Subelement nome
nome = SubElement(raiz, "nome")
nome.text = 'Carlos Silva'

# Subelement cpf
cpf = SubElement(raiz, "cpf")
cpf = '142.142.142-14'

# Subelement endereço
endereco = SubElement(raiz, "endereco")
endereco.text = 'Rua 1, 2 - 3 - 4'

# Subelement contato
contato = SubElement(raiz, "contato")

# Elemento com Subelementos
telefone = SubElement(contato, 'telefone')
telefone.text = '(11) 969696969'

email = SubElement(contato, 'email')
email.text = 'carlos.silva@gmail.com'

# Gerar o arquivo
ElementTree(raiz.write('cadastro.xml'))