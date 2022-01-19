from socket import *

port = 8080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', port))

# 1. 로컬서버 (127.0.0.1)의 8080포트에 연결한다.

print('클라이언트 접속 완료')


while True :
    received_data = client_socket.recv(1024)                # 2. 서버에서 받은 값을 저장해서 print한다.
    print('서버측 메시지 : ', received_data.decode('utf-8')) 

    send_data = input('>>>')                                # 3. '>>>'를 출력 후 값을 저장한다.
    client_socket.send(send_data.encode('utf-8'))           # 4. 데이터를 서버에 전송한다. 2번부터 반복한다.