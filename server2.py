import socket

'''The primary purpose of AF_INET was to allow for other possible network 
protocols or address families (AF is for address family;
PF_INET is for the (IPv4) internet protocol family)'''

#SOCK_STREAM means that it is a TCP socket.

#What if you wanted to use UDP socket? -SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#You declare your server host and port to establish a connection  
host = '192.168.10.60'
port = 5000

#s.bind() is a function under the 'socket' library imported above
#this expects 2 parameters... an ipv4 address and a port
#take note that the ip address should be written as a string

s.bind((host, port))

#display a message so we know we had successfully bind
print ('Socket binded to port ' + str(port))

#s.listens() is also a function that expects 1 parameter which will be maximum number of machine
#that is allowed to connect to the server
s.listen(3)
print ('socket is listening')

#this is a python while loop
#its set to true so it will always check if there are incomming connections to the server
while True:

    #s.accept() is a function that returns 
    # two values where 'c' is a new socket object usable to send and receive data on the connection
    #and 'addr' is the address bound to the socket on the other end of the connection
    c, addr = s.accept()

    print ('Got connection from ', addr)
    print (c.recv(1024))
    
    c.close()