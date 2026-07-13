import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("10.76.166.126", 5000))

print("Waiting for message...")

msg, addr = s.recvfrom(1024)

print("Message:", msg.decode())

s.close()