import socket

SERVER_IP = "172.21.224.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter Message: ")

client.sendto(message.encode(), (SERVER_IP, PORT))

print("Message is sent.")

client.close()