from config import UDP_IP, UDP_SERVER_PORT, UDP_SIGNAL_PORT 
from pi_sock import create_output_socket, create_input_socket 

inputSocket = create_input_socket(UDP_IP, UDP_SERVER_PORT)
outputSocket = create_output_socket()

try:
    while True:
        data, addr = inputSocket.recvfrom(1024) # buffer size is 1024 bytes
        print "Addr:", addr[0]
        outputSocket.sendto("me!",(UDP_IP, UDP_SIGNAL_PORT))
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()