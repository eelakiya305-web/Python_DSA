import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5000

server.bind((host, port))
server.listen(1)


print("Waiting for client...")

conn, addr = server.accept()
print("Connected by:", addr)

# Receive message from client
msg = conn.recv(1024).decode()
print("Client:", msg)

# Server user input
reply = input("Enter reply: ")
conn.send(reply.encode())

conn.close()
server.close()