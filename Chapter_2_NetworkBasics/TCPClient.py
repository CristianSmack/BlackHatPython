import socket

# Target host
target_host = "127.0.0.1"
target_port = 9999

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
    AF_INET: this parameter is saying we are going to use a standar IPV4
    address or a hostname
    
    SOCK_STREAM: this parameter indicates that this client will be a TCP
    client 

"""

# Connect the client
client.connect((target_host, target_port))

# Send some data
client.send(bytes("GET / HTTP/1.1/\r\nHost: google.com\r\n\r\n", encoding="UTF-8"))

# Receive the response
response = client.recv(4096)

# Show the response
print(response)

"""
    In this code snippet we assume that the connection
    always success and the server will always send us a 
    response
"""