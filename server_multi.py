from socket import *
import threading
def threaded(c, add):
    while True:
        data = c.recv(1024)
        if data.decode() == "over":
            print('Terminated', add)
            break
        print(add, data.decode())
    c.close()

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(("", 1200))
ss.listen(5)
while True:
    conn, add = ss.accept()
    thread = threading.Thread(target = threaded, args =(conn, add))
    thread.start()
    print('Connected to: ', add[0], ':', add[1])
ss.close()
