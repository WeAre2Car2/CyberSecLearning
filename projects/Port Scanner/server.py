import socket

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
server.bind(('127.0.0.1', 6969)) # Bind to localhost on port 6969
server.listen(5) # Listen for incoming connections
print("Server is listening on port 6969...")

while True:
    client, address = server.accept()
