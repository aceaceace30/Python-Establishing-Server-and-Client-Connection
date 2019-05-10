import socket
import sys

'''The primary purpose of AF_INET was to allow for other possible network 
protocols or address families (AF is for address family;
PF_INET is for the (IPv4) internet protocol family)'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.10.60'
port = 5000
s.bind((host, port))
print ('Socket binded to port ' + str(port))
s.listen(3)
print ('socket is listening')

while True:
    c, addr = s.accept()
    print ('Got connection from ', addr)
    print (c.recv(1024))
    c.close()