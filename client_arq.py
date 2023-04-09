from socket import *
import random
cs = socket(AF_INET,SOCK_STREAM)
cs.connect((gethostname(),1900))
print("Connected")
m = int(input("Enter m: "))
val = 2**(m-1)
cs.send(str(val).encode())
frame_b = random.randint(10, 100)
for i in range(val):
    cs.send(str(frame_b).encode())
    print("Frame Sent:", frame_b)
    ch = int(cs.recv(1024).decode())
    print("Acknowledgement Recieved:", ch)
    if(ch!=frame_b):
        frame_b += val
cs.close()
    
