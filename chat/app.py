import modules.database as database
import threading

if __name__ == "__main__":
    user = input('Username: ')
    try:
        tr = threading.Thread(target=database.selectMessage)
        tr.start()
    except Exception as e:
        print(f'Falha ao criar a thread: {e}')
    
    while tr.isAlive:
        menssage = input()
        database.insertMessage(user, menssage)
