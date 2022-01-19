from socket import *

port = 8080

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',port))
# 1. 접속을 받는 상태로 변경
server_socket.listen(1)                     

print(f'{port}번 포트로 접속 대기중 ..')

# 2. 누군가가 접속하면 accept()에서 return이 발생한다.
# 2-1. 이 return에는 연결된 socket이 포함된다.
connection_socket, address = server_socket.accept()

print(str(address), '에서 접속되었습니다.')

while True :
    send_data = input('>>>')                            # 3. '>>>'의 출력과 함께 콘솔에서 입력을 받는다.
    connection_socket.send(send_data.encode('utf-8'))   # 4. 입력받은 값을 encode해서 소켓에 전달한다.

    received_data = connection_socket.recv(1024)        # 5. 연결된 소켓에서 받은 값을 decode해서 저장한다.
    print('상대방 메시지: ', received_data.decode('utf-8'))# 6. print하고 3번을 반복한다.

