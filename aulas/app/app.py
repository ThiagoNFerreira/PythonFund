import e_comerce

# Instâncias

item01 = e_comerce.Item('Camiseta São Paulo', preco=159)
item02 = e_comerce.Item('Camiseta Xadrex', preco=99)
item03 = e_comerce.Item('Camiseta Bob Esponja', preco=80)
cliente01 = e_comerce.cliente()

cliente01.adiciona_item(item01)
cliente01.adiciona_item(item02)
cliente01.adiciona_item(item03)

print(cliente01.consolidar_carrinho())
