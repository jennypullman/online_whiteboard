import socket
import asyncore

a = asyncore.dispatcher()
server_socket = a.create_socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind((socket.gethostname(),1242))
a.listen(5)
print "yesssss"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

accepted = False
connected = False
while 1:
    if not accepted:
        try:
            conn, addr = a.accept()
            #conn.setblocking(1)
            accepted = True
            print "accepted"
        except TypeError:
            accepted = False
    if not connected:
        try:
            s.connect(('192.168.1.10', 1242))
            connected = True
            print "connected"
        except:
            connected = False
    if accepted and connected:
        break
print "worked"
    
info_sent = False

while 1:
    while 1:
        try:
            data = conn.recv(1024)
            if not data: break
            #conn.sendall(data)
            print data
            print "damn"
        except:
            break
    if info_sent == False:
        try:
            s.sendall("whats gooood")
            info_sent = True
        except:
            continue
conn.close()

print "complete"
