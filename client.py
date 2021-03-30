import threading
import socket

nickname=input("choose a nick name: ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

def recieve():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=="NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!!")
            client.close()
            break

def write():
    while True:
        message=f'{nickname} : {input("")}'
        client.send(message.encode('utf-8'))





receve_tread=threading.Thread(target=recieve)
receve_tread.start()

write_thread=threading.Thread(target=write())
write_thread.start()

