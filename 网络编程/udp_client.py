import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# client.bind(('127.0.0.1', 420))

while True:

    send = input()
    addr = ('127.0.0.1', 520)
    client.sendto(send.encode('utf-8'), addr)
    # data, addr = client.recvfrom(1024)
    data = client.recv(1024).decode('utf-8')
    print("Recerived from {} ---->{}".format(addr, data))
