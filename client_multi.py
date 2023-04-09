from socket import *
cs = socket(AF_INET, SOCK_STREAM)
cs.connect((gethostname(),1200))
while True:
    in1 = input("Enter text: ")
    if in1=="over":
        cs.send(in1.encode())
        break
    else:
        cs.send(in1.encode())
cs.close()
    
