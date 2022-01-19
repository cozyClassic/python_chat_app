from socket import *
import threading
import time

def send(sock) :
    # 메시지 전송 시 필요한 함수
    send_data = input('>>>')
    sock.send(send_data.encode('utf-8'))
    

def receive(sock) :
    # 메시지 수신 시 필요한 함수
    received_data = sock.recv(1024)
    print('상대방 : ', received_data.decode('utf-8'))


port = 8081


server_socket = socket(AF_INET, SOCK_STREAM)
# 서버 유형 : ipv4, stream
server_socket.bind(('', port))
# 포트 설정 : 전체 접속을 8080포트로

server_socket.listen(1)
print(f'{port}번 포트로 접속 대기중 ...')
# True(1) 상태로 항상 접속 받을 수 있게 대기

connection_socket, address = server_socket.accept()
# 접속 발생 시 소켓과 주소 확인

print(str(address), '에서 접속되었습니다.')


# send 함수와 receive 함수를 threading.Thread()로 생성한다.
sender = threading.Thread(target=send, args=(connection_socket,))
receiver = threading.Thread(target=receive, args=(connection_socket,))
# Thread(타겟=스레드가 실행할 함수, 인자=함수에 전달할 인자)
# args는 튜플같이 iterable한 변수만 입력될 수 있다.
# 다만 args가 딱 하나일 때에도, 튜플로 인식시키기 위해 뒤에 쉼표를 붙여주어야 한다.

sender.start()
receiver.start()
# 스레드를 실행한다.

while True :
    # 이 server.py가 계속 실행되는 상태로 있게 하기 위해
    time.sleep(1)
    pass

