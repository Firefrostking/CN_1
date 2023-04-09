from socket import *
cs = socket(AF_INET,SOCK_STREAM)
cs.connect((gethostname(),1900))
file = open("C:\\Users\\ASUS\\Documents\\cn fatlab\\input.txt","r")
data = file.read()
cs.send(data.encode())
cs.close()
