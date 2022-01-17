from socket import socket, AF_INET, SOCK_STREAM

# 클라이언트 소켓을 사용하는 법

client_sock = socket(AF_INET, SOCK_STREAM)
client_sock.connect(('127.0.0.1', 8080))

# bind 와 listen, accept 과정이 빠진 대신 connect가 추가되었다.
# 소켓 송수신

print('연결 확인')
client_sock.send('I am a client'.encode('utf-8'))

print('메시지 from 클라이언트')

data = client_sock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))