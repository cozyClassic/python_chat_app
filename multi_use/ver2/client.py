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

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', port))

print('클라이언트 접속 완료')

sender = threading.Thread(target=send, args=(client_socket,))
receiver = threading.Thread(target=receive, args=(client_socket,))

sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass
