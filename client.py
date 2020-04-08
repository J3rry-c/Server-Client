import socket

#creating socket :

c = socket.socket()

#connecting to the server :

c.connect(("localhost",9999))

# receiving data:

def reciev():

    message_recieved = c.recv(1024)
    print(message_recieved.decode())

#sending data :

def send():

  data = input('mess: ')
  c.send(bytes(data,"utf-8"))



while True :
    reciev()
    send()

