from socket import *
cs = socket(AF_INET,SOCK_STREAM)
cs.connect((gethostname(),1240))
while True:
    in1 = input("Enter Text: ")
    if in1 == "over":
        cs.send(in1.encode())
        break
    else:
        cs.send(in1.encode())
        sm = cs.recv(1024)
        print("Server:",sm.decode())
cs.close()
