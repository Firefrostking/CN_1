from socket import *
port = 1200
ss = socket(AF_INET,SOCK_STREAM)
ss.bind(("",1200))
ss.listen(5)
conn,add = ss.accept()
print("Connection established")
while True:
    in1 = conn.recv(50)
    on1 = in1.decode()
    conn.send(on1.encode())
    print("Sent Back")
