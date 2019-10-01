import socket

UDP_IP = "255.255.255.255"
UDP_PORT = 2345

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    
    print "Addr:", addr[0]

