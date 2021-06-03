import socket
import struct
import sys
import time

master = ("xxx.com",xxxx)

try:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockfd.bind(('',0))
    sockfd.sendto("Hello",master)

except socket.error:
    print "Failed to create socket"
    sys.exit()

# Receiving peer info from server

peer_data, addr = sockfd.recvfrom(1024)
print peer_data


print "Trying to communicate with peer"
peer_i = peer_data.split(':')[0]
peer_port = int(peer_data.split(':')[1])

for i in range(100):
    print "sending"
    sockfd.sendto("Hello from your peer client A",(peer_ip,peer_port))
    time.sleep(0.5)
