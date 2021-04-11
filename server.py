import socket
from _thread import *



server = "192.168.1.102"   #ip adress (my local one)
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #always like that

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)   #opens the port. if the function is left balnk, unlimitend connections will happen
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)  #gets information from who is connected. The argument are the bits recevied
            reply = data.decode("utf-8")   #decodes the informations we get so people can read it
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))  #encodes again the informations decoded earlier
        except:
            break
    print("Connection lost")
    conn.close()
while True: #constantly looking for connections
    conn, addr = s.accept()   #accepts the connections that occure
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))   #lets the function run in the backround, without having to wait for it to finish
