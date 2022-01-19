import _thread
from socket import *

_thread.start_new_thread()

port = 8080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', port))

print('클라이언트 접속 완료')

while True :
    received_data = client_socket.recv(1024)
    print('서버측 메시지 : ', received_data.decode('utf-8'))

    send_data = input('>>>')
    client_socket.send(send_data.encode('utf-8'))

