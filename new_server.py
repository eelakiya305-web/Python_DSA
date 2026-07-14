import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Waiting for message...")


data, addr = server.recvfrom(1024)

print("Message is received.")
print("Received Message:", data.decode())

server.close()