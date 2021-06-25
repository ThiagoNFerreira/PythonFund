# Testes Unitários
from unittest import TestCase, main
from cliente import Cliente
from item import Item

class testCliente(TestCase):

    def test_consolidar_compra(self):
        cliente01 = Cliente('Jorge', 'teste@gmail.com', '13245678942')
        p1 = Item('Item de Test', preco=100)
        p2 = Item('Item de Test2', preco=200)

        cliente01.adiciona_item(p1.make_item())
        cliente01.adiciona_item(p2.make_item())
        self.assertEqual(300, cliente01.consolidar_compra())
    
    def test_remover_item(self):
        cliente02 = Cliente('Jorge', 'teste@gmail.com', '13245678942')
        p4 = Item('Item de Test', preco=100)
        p5 = Item('Item de Test2', preco=200)
        p6 = Item('Item de Test2', preco=20)
        

        cliente02.adiciona_item(p4.make_item())
        cliente02.adiciona_item(p5.make_item())
        cliente02.adiciona_item(p6.make_item())

        cliente02.remover_item(p5.make_item())

        self.assertEqual(120, cliente02.consolidar_compra())

class testsItem(TestCase):

    def test_make_item(self):
        nome = 'Teste01'
        descricao = 'apenas um test'
        preco = 200

        item1 = Item('Teste01', descricao='apenas um test', preco=200)

        test_item = {
            'nome': nome,
            'descricao': descricao,
            'preco': preco
        }

        self.assertDictEqual(test_item, item1.make_item())

if __name__ == '__main__':
    main()