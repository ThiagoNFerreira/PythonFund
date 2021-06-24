class cliente():

    def __init__(self, nome='', email='', cpf=0, carrinho=[], total=0):
        self.__carrinho = carrinho
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__total = total
    
    # Métodos comportamentais
    def adicionaItem(self, item):
        self.__carrinho.append(item)

    def ver_carrinho(self):
        print(self.__carrinho)
    
    def remover_item(self, item):
        self.__carrinho.remove(item)
    
    def consolidar_compra(self):
        for item in self.__carrinho:
            self.__total += item["preco"]
        return self.__total


