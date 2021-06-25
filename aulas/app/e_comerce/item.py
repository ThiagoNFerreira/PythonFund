class Item():

    # Método construtor
    def __init__(self, nome, descricao='', preco=0):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
    
    def make_item(self):
        self.item = {
            'nome': self.__nome,
            'descricao': self.__descricao,
            'preco': self.__preco
        }
        return self.item
        
    # Métodos de acesso
    def get_nome(self):
        return self.__nome
    
    def get_desc(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco
    
    # Métodos de definicao
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco
    
    def set_desc(self, descricao):
        self.__descricao = descricao
