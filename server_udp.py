from socket import *
ss = socket(AF_INET,SOCK_DGRAM)
ss.bind(("",1240))
ss.listen(5)
conn,add = ss.accept()
while True:
    in1 = conn.recvfrom(1024)
    if in1.decode() == "over":
        break
    print("Client: ",in1.decode())
    on1 = input("Enter msg: ")
    conn.sendto(on1.encode())
    print("Sent")
conn.close()
