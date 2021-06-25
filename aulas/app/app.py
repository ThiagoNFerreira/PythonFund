import e_commerce

# Instancias
item01 = e_commerce.Item('Camiseta Corinthinas', preco=159)
item02 = e_commerce.Item('Camiseta Xadrex', preco=99)
item03 = e_commerce.Item('Caneca Bob Sponja', preco=199)
cliente01 = e_commerce.Cliente()


cliente01.adiciona_item(item02.make_item())
cliente01.adiciona_item(item02.make_item())
cliente01.adiciona_item(item03.make_item())

print(cliente01.consolidar_compra())