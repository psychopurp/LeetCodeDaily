import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# client.bind(('127.0.0.1', 510))
client.connect(('127.0.0.1', 520))


def tcp_recv(sock: socket.socket):
    while True:
        if not flag:
            break
        data = sock.recv(1024).decode('utf-8')
        print('Server >> {}'.format(data))
    print('thread {} ended.'.format(threading.current_thread().name))


flag = True
rcv_thread = threading.Thread(
    target=tcp_recv, args=(client,))
rcv_thread.start()


while flag:
    # print("发送数据 >> ", end='')
    send = input()
    client.send(send.encode('utf-8'))
    if send == 'exit':
        flag = False
client.close()
