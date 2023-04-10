from socket import *
import random
ss = socket(AF_INET,SOCK_STREAM)
ss.bind(("",1900))
ss.listen(5)
print("Waiting for client....")
conn, add = ss.accept()
print("Connection established")
val = int(conn.recv(1024).decode())
arr1 = []
for i in range(val):
    arr1.append("0")
r = random.randint(0, val)
arr1[r] = "-1"
for i in range(val):
    if arr1[i]!="-1":
        frame_num = int(conn.recv(1024).decode())
        print("Frame:", frame_num)
        print("Window size:", i+1, "to", val+i)
        ack = frame_num + val
        ac = str(ack)
        conn.send(ac.encode())
        print("Acknowledgement sent:", ack)
    else:
        frame_num = conn.recv(1024).decode()
        print("Frame:", -1)
        i = i-1
        print("Window size:", i+1, "to", val+i)
        ack = frame_num
        conn.send(ack.encode())
        print("Acknowledgement sent:", ack)
ss.close()
