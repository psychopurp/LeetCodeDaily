import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.bind(('127.0.0.1', 520))

while True:
    data, addr = server.recvfrom(1024)
    print("Recerived from {} ---->{}".format(addr, data.decode('utf-8')))
    send = input()
    server.sendto(send.encode('utf-8'), addr)
