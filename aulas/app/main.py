# Orientação a objetos

# Paradigma de programação - Resolver um tipo de problema

## Escrevemos códigos até agora usando o paradigma procedural (linear) e funcional.

# Problemas que o paradigma orientado a objetos resolve:

# - Reutilização do código
# - Centralização dos dados
# - Aumento do tamanho

# Através do paradima de Programação Orientado a Objeto, temos:

# Capacidade de manipular os dados de forma a respeitar as regras de negócio
# Restringir o acesso aos dados



# Conceitos:



# Abstração - Isolar a nossa lógica, mantendo o usuário sem a necessidade de compreender o todo. "print()" é usado sem saber toda sua estrutura de criação.
# Encapsulamento - Isolar seus atributos do cliente (Colocar o __ no atributo "__atributo")
# Herança - Herdar atributos e métodos de outro objeto.
# Polimorfismo - mesmo herdando características, eu posso alterar essas características na classe que herdou sem afetar o objeto inicial.

# class Casa01():
#     def __init__(self): # self é uma referência ao objeto para associar a instância do objeto
#         self.quartos = 2
#         self.sala = 1
#         self.banheiro = 2
#         self.garagem = 2
#         self.cozinha = 'Americana'

#     def informacoes(self):
#         print({self.quartos})
#         print({self.garagem})
#         print({self.cozinha})
#         print({self.banheiro})
#         print({self.sala})
    
#     def construirCasa(self):
#         print('Casa construída')


# casaPedro = Casa01()
# casaPedro.informacoes()
# casaPedro.cozinha = 4

# casaPaulo = Casa01()
# casaPaulo.informacoes()

# class automovel():
#     def __init__(self):
#         self.motor = True
#         self.rodas = 4
#         self.portas = 2

#     def ligar(self):
#         pass

#     def desligar(self):
#         pass

#     def acelerar(self):
#         pass

#     def frear(self):
#         pass

# hb20 = automovel()

# class contaCorrente():

#     def __init__(self):
#         self.__nomeCliente = input('Nome de cliente: ')
#         self.__idBanco = 777
#         self.__idAgencia = int(input('Digite o número da agência: '))
#         self.__saldo = 0
    
#     def extrato(self):
#         print('----Extrato-----')
#         print(f'Nome: {self.__nomeCliente}')
#         print(f'Saldo: {self.__saldo}')

#     def sacar(self, valor):
#         if self.__saldo >= valor:
#             print(f'Saldo anterior: {self.__saldo}')
#             self.__saldo -= valor
#             print(f'Novo Saldo: {self.__saldo}')
#         else:
#             print('Saldo insuficiente')

#     def transferencia(self, valor):
#         print(f'Saldo anterior: {self.__saldo}')
#         self.__saldo +=valor
#         print(f'Novo saldo: {self.__saldo}')
    
#     def alterarNome(self, nome):
#         self.__nomeCliente = nome
#         print('Nome alterado')

# class Colaborador():

#     def __init__(self):
#         self.__nome = input('Nome: ')
#         self.__matricula = input('Matrícula: ')
#         self.__endereco = input('Endereco: ')
#         self.__dataNascimento = input('Data de nascimento: ')
#         self.__salario = 2500
#         self.__funcao = 'N1'

#     def funcao(self):
#         print(f'Trabalhando {self.__funcao}')

# class ColaboradorN2(Colaborador):

#     def __init__(self):
#         Colaborador().__init__()


# Herança

class Pai():

    def __init__(self):
        self.nome = 'Joao'
        self.sobrenome = 'Pereira Pinto'
        self.profissao = 'Marceneiro'

    def trabalhar(self):
        print(f'Trabalhando como {self.profissao}')

class Filho(Pai):
    def __init__(self):
        super().__init__()
        self.nome = 'Carlos'
        self.profissao = 'Menino do TI'



# Palavras-chaves:


# Objeto - Uma instância de uma classe
# Classe - Definição de como o objeto deve ser
# Método construtor - Método que inicializa atributos na criação do objeto
# Instância - Variável que contém a classe
# Atributo - Característica
# Método - ações da classe
# self - Referencia ao objeto












