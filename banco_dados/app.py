# # import sqlite3
# # from sqlite3.dbapi2 import Cursor

# # # Criando a conexao com o banco
# # con  = sqlite3.connect('banco.db')

# # # Criar um cursosr - serve apontarsu
# # cursor = con.cursor()

# # SQL_STRING = """
# # create table produto(
# #     id integer primary key autoincrement,
# #     nome text,
# #     desc text,
# #     preco real,
# #     ativo boolean
# # );
# # """
# # try:
# #     cursor.execute(SQL_STRING)
# #     con.commit()
# # except Exception as e:
# #     print(e)
# #     con.rollback()
# # finally:   
# #     con.close()


# import psycopg2
# import getpass

# senha = getpass.getpass()
# conexao = psycopg2.connect(f'host= localhost dbname=projeto user=admin password={senha}')

# cursor = conexao.cursor()

# def insertUsuario():
#     nome = input('Digite o nome do usuário: ')
#     email = input('Digite o nome do email: ')
#     endereco = input('Digite o nome do endreco: ')

#     try:
#         cursor.execute(f"insert into usuarios(nome, email, endereco) values ('{nome}', '{email}', '{endereco}');")
#         conexao.commit()
#         print('Dados Inseridos')
#     except Exception as e:
#         print(f'ERRO: {e}')
#         conexao.rollback()
#     finally:
#         print('Conexao finalizada')
#         conexao.close()

# def selectUsuario():
#     user_id = input('Id: ')
#     cursor.execute(f"select * from usuarios where id={user_id};")
#     print(cursor.fetchall())

# def deleteUsuario():
#     user_id = input('Id: ')
#     try:
#         cursor.execute(f"delete from usuarios where id={user_id};")
#         conexao.commit()
#         print('Dados Deletados')
#     except Exception as e:
#         print(f'ERRO: {e}')
#         conexao.rollback()
#     finally:
#         print('Conexao finalizada')
#         conexao.close()
    
# def updateUsuario():
#     pass

# #insertUsuario()
# #selectUsuario()
# deleteUsuario()

from pymongo import MongoClient

client = MongoClient("localhost")
db = client['clientes']

def insertDocument():
    nome = input('nome: ')
    idade = input('Idade: ')
    valorDivida = float(input('Valor da Dívida: '))
    try:

        db.cadastro.insert_one({
            "nome": nome,
            "idade": idade,
            "valorDivida": valorDivida
        })
    except Exception as e:
        print(e)

def findDocument():
    for document in db.cadastro.find():
        print('=============')
        print(document)
        
def deletDocument():
    user_id = input('Informe o ID: ')
    try:

        db.cadastro.remove({
            "id": user_id
        })
    except Exception as e:
        print(e)



#insertDocument()
#findDocument()
deletDocument()