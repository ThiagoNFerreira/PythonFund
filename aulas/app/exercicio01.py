# Crie uma Classe Colaborador que tenha atributos e métodos
# Crie uma Classe Gerente que herde de Colaborador e altere a funcao e salario
# Crie uma Classe suporteN1 que herde de Colaborador e altere funcao e salario

class Colaborador():

    def __init__(self):
        self.nome = input('Nome: ')
        self.salario = 0
        self.funcao = None

    def trabalhar(self):
        print(f'Funcionário {self.nome}\nFunção {self.funcao}\nSalário {self.salario}')

class Gerente(Colaborador):

    def __init__(self):
        super().__init__()
        self.salario = 5000
        self.funcao = "Gerente"
        

class suporteN1(Colaborador):

    def __init__(self):
        super().__init__()
        self.salario = 1000
        self.funcao = "suporte N1"

c01 = Gerente()
c01.trabalhar()

c02 = suporteN1()
c02.trabalhar()

