import threading
import socket
from Crypto.Cipher import AES
import hybrid_encription as hy
host="127.0.0.1"
port=55555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)
        encription(message.decode('utf-8'))

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)


        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def recive():
    while True:
        client,address=server.accept()
        print(f'connected with{str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nick name of the client{nickname}!')
        broadcast(f'{nickname} joind the chat!'.encode('utf-8'))
        client.send('connect to the server'.encode('utf-8'))


        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

print(("server listning...."))


def encription(plainText):
    print("Generating RSA public and Private keys......")
    pub, pri = hy.KeyGeneration()

    # Generates a fresh symmetric key for the data encapsulation scheme.
    print("Generating AES symmetric key......")
    key = hy.secrets.token_hex(16) #The secrets module provides functions for generating secure tokens, suitable for applications such as password resets, hard-to-guess URLs, and similar.
    print("AES Symmetric Key: ")
    print(key)
    KeyAES = key.encode('utf-8')

    # Encrypts the message under the data encapsulation scheme, using the symmetric key just generated.

    cipherAESe = AES.new(KeyAES, AES.MODE_GCM)
    nonce = cipherAESe.nonce #It use only one time
    print("Encrypting the message with AES......")
    cipherText = hy.encryptAES(cipherAESe, plainText)
    print("AES cypher text: ")
    print(cipherText)

    # Encrypt the symmetric key under the key encapsulation scheme, using Alice’s public key.
    cipherKey = hy.encrypt(pub, key)
    print("Encrypting the AES symmetric key with RSA......")
    print("Encryted AES symmetric key")
    print("cipher text=",cipherKey)

    # Uses her private key to decrypt the symmetric key contained in the key encapsulation segment.
    decriptedKey = ''.join(hy.decrypt(pri, cipherKey))
    print("Decrypting the AES Symmetric Key...")
    print("AES Symmetric Key:")
    print(decriptedKey)

    # Uses this symmetric key to decrypt the message contained in the data encapsulation segment.
    decriptedKey = decriptedKey.encode('utf-8')
    cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
    decrypted = hy.decryptAES(cipherAESd, cipherText)
    print("Decrypting the message using the AES symmetric key.....")
    print("decrypted message: ")
    print(decrypted)
    return decrypted



recive()

