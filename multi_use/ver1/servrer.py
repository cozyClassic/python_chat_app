from audioop import add
from socket import *

port = 8080

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',port))
server_socket.listen(1)

print(f'{port}번 포트로 접속 대기중 ..')

connection_socket, address = server_socket.accept()

print(str(address), '에서 접속되었습니다.')

while True :
    send_data = input('>>>')
    connection_socket.send(send_data.encode('utf-8'))

    received_data = connection_socket.recv(1024) # 1024 = 바이트 크기
    print('상대방 메시지: ', received_data.decode('utf-8'))

