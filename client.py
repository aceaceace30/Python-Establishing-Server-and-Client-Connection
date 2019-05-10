import socket

s = socket.socket()
host = '192.168.10.60'
port = 5000
s.connect((host, port))
z = 'Your string'
s.sendall(z.encode())    
s.close()