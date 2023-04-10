from socket import *
ss = socket(AF_INET,SOCK_DGRAM)
ad1 = ("",1240)
ss.bind(("",1240))
while True:
    in1, add = ss.recvfrom(1024)
    if in1.decode() == "over":
        break
    print("Client: ",in1.decode())
    on1 = input("Enter msg: ")
    ss.sendto(on1.encode(), add)
    print("Sent")
ss.close()
