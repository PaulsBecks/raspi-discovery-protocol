import socket

def create_output_socket () : 
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  return s



def create_input_socket (ip, port) :
  s = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
  s.bind((ip, port))
  return s