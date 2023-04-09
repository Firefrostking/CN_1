from socket import *
cs = socket(AF_INET, SOCK_STREAM)
cs.connect((gethostname(),1200))
while True:
    in1 = input("Enter input: ")
    if in1 == "over":
        break
    else:
        cs.send(in1.encode())
        ps = cs.recv(50)
        print(ps.decode())
cs.close()
