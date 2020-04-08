import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(('127.0.0.1', 520))
server.listen(5)


def tcp_recv(sock: socket.socket, addr):
    while True:
        data = sock.recv(1024).decode('utf-8')
        print('Client >> {}     [ from {} ]'.format(data, addr))
        if data == 'exit':
            break
    print('thread {} ended.'.format(threading.current_thread().name))


def tcp_link(sock: socket.socket, addr):
    print("Accept new connection from {}".format(addr))
    sock.send(b"welcome")
    rcv_thread = threading.Thread(target=tcp_recv, args=(sock, addr))
    rcv_thread.start()
    while True:
        if not rcv_thread.is_alive():
            print("thread {} not alive".format(rcv_thread))
            break
        # print("发送数据 >>", end='')
        send = input()
        sock.send(send.encode('utf-8'))

    sock.close()
    print("Connection from {} closed".format(addr))


while True:
    print("listenning port 520")
    sock, addr = server.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    print('创建线程 {} 来处理'.format(t))
    t.start()
