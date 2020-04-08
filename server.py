import socket

# creating socket :

s = socket.socket()

# Triying to connect socket :

host = "localhost"
port = 9999

s.bind((host,port))
s.listen(3)
print("waiting for connections! ")

# accepting socket  :

conn, addr = s.accept()
print("conneted with : ", "\n", addr)

 # sending & recieving data (chatting):

def send():

        data = input("mess : ")
        conn.send(bytes(data, "utf-8"))


def reciev():

        data_back = conn.recv(1024)
        print(data_back.decode())

def main():
        send()
        reciev()

while True :
     main()






