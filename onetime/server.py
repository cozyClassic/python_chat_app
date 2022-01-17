from socket import socket, AF_INET, SOCK_STREAM

server_sock = socket(AF_INET, SOCK_STREAM)
# 서버 객체 생성
# 인자 1. AF_INET = 어드레스 패밀리(AF) (IPv4) (AF_INET6 == IPv6)
# 인자 2. 소켓타입. SOCK_STREAM과 SOCK_DGRAM만이 주로 사용된다.

server_sock.bind(('', 8080))
# 생성한 소켓을 bind 해주기
# 클라이언트에는 불필요하다. 서버에는 필요하다.
# 이 작업이 의미하는 바는, 생성된 소켓의 번호와 실제 어드레스 패밀리를 연결해 주는 것이다.
# 인자 1. 튜플. (ip, port) 형식이다.
# ip 인자의 빈 값은 INADDR_ANY를 의미한다. 즉, 모든 인터페이스와 연결할 때 사용한다.
# 결론적으로 모든 인터페이스를 8080포트와 연결한다.

server_sock.listen(1)
# 상대방의 접속을 기다리는 단계가 된다.
# 인자 1. 숫자 = 소켓이 총 몇개의 동시 접속까지를 허용할 것이냐


connection_sock, addr = server_sock.accept()
# 접속을 수락하고, 그 후에 통신을 하기 위해 필요한 것
# accept()

# accpet()는 소켓에 누군가가 접속하여 연결이 되었을 때 return 이 발생하는 함수이다.
# 즉, 소스코드 내에 accept()가 있더라도, 누군가가 접속할 때까지 프로그램은 이 부분에서 멈춰있게 된다.
# accept()가 실행 되면, return 값으로 새로운 소켓과 상대방의 AF(IPv4)를 전달해주게 된다.
# 이후, 서버에 접속한 상대방과 데이터를 주고 받기 위해서는 accept()를 통해 생성된 connection_sock를 사용한다.

print(str(addr), '에서 접속이 확인 되었습니다.')

data = connection_sock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connection_sock.send('I am server'.encode('utf-8'))
print('메시지 from 서버')
