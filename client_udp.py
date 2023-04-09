from socket import *
cs = socket(AF_INET,SOCK_DGRAM)
cs.connect((gethostname(),1240))
while True:
    in1 = input("Enter Text: ")
    if in1 == "over":
        cs.sendto(in1.encode())
        break
    else:
        cs.sendto(in1.encode())
        sm = cs.recvfrom(1024)
        print("Server:",sm.decode())
cs.close()
