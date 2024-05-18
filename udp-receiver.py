# UDP RECEIVER
import socket
from time import sleep

server_address = ("127.0.0.1", 20001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
   msg, sender = sock.recvfrom(4096)
   print(f"Received {msg} from {sender}")
   sleep(1)