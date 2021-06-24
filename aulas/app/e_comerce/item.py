class Item():
    # Método construtor
    def __init__(self, nome, descricao, preco):
        self.__item = {
        "nome":nome,
        "descricao":descricao,
        "preco":preco
    }
    # Métodos de acesso
    def get_item(self):
        return self.__item

    def get_nome(self):
        return self.__item["nome"]

    def get_desc(self):
        return self.__item["descricao"]
    
    def get_preco(self):
        return self.__item["preco"]

    # Métodos de definição
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_desc(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco
    
    