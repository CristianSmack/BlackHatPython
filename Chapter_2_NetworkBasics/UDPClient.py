import socket

target_host = "127.0.0.0"
target_port = 80

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
    AF_INET: this parameter is saying we are going to use a standar IPV4
    address or a hostname

    SOCK_DGRAM: this parameter indicates that this client will be a UDP
    client 

"""

# Send some data
client.sendto(b"AAABBBCCC", (target_host,target_port))

# Receive some data
data, addr = client.recvfrom(4096)

# Show response
print("Address: {}".format(addr))
print("Data: {}".format(data))

"""
    We assume that we have an UDP server running in our localhost 
    listening in port 80
"""