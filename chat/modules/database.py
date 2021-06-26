from pymongo import MongoClient, DESCENDING
import time

from pymongo.message import update


MONGO_URI = 'mongodb+srv://admin:4linux@aulamongo.d8erp.mongodb.net/chat?retryWrites=true&w=majority'
try:
    client = MongoClient(MONGO_URI)
    db = client['chat']
except Exception as e:
    print(f'ERRO: {e}')
    exit()

def insertMessage(name, message):
    msg = {
        'nome': name,
        'mensagem': message,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(msg)

def selectMessage():
    lastMessage = [msg for msg in db.chat.find().sort("_id", DESCENDING)]
    
    while True:
        updateMessage = [msg for msg in db.chat.find().sort("_id", DESCENDING)]
    
        if lastMessage != updateMessage:
            lastMessage = updateMessage
            print(f"[{updateMessage[0]['hora']}] {updateMessage[0]['nome']} : {updateMessage[0]['mensagem']}")
        time.sleep(2)
