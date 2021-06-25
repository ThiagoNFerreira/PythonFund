# try:
#     with open('arquivo.txt', 'r+') as arquivo:
#         arquivo.read()

# except Exception as e:
#     print(e)
#     with open('arquivo.txt', 'x') as arquivo:
#         arquivo.write('Arquivo Criado')

# finally:
#     print('Tratamento cocluído')

from datetime import datetime

try:
    arquivo = open('arquivo003', 'r')
    arquivo.read()
    arquivo.write('Arquivo existente')

except Exception as e:
    print(e)
    arquivo = open('arquivo003', 'x+')
    arquivo.write(f'arquivo criado em {datetime.now()}')

else:
    arquivo.close()

finally:
    print('Tratamento concluído')

