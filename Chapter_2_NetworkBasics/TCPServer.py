import socket
import threading

# Localhost
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
    AF_INET: this parameter is saying we are going to use a standar IPV4
    address or a hostname

    SOCK_STREAM: this parameter indicates that this client will be a TCP
    server 

"""


# With bind, we are telling that we start a server
server.bind((bind_ip, bind_port))

# The server is listening with a max of 5 client
server.listen(5)

print("[INFO] Listenting on {}:{}".format(bind_ip,bind_port))

"""
    Method for handle clients with threading
    Performs the recv() function and it sends
    a simple message back to the client
"""
def handle_client(client_socket):

    # Print the client request
    request = client_socket.recv(1024)

    print("[INFO] Received: {}".format(request))

    # send back a message (needs to be bit)
    client_socket.send(b"Received!!")

    # Close the client socket

while True:

    """
        client: saves the client socket 
        addr: remote connection details
    """
    client, addr = server.accept()

    print("[INFO] Accepted connection from {}:{}".format(addr[0],addr[1]))

    # Spin up the client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()