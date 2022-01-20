import threading
import time
from queue import Queue
from socket import *

def Send(group, send_queue) :
    print("SEND thread 시작")
    while True :
        try :
            # 새롭게 추가된 클라이언트가 있을 경우
            # send 쓰레드를 새롭게 만들기 위해 루프를 빠져 나감
            recv = send_queue.get()
            if recv == 'Group Changed' :
                print('Group changed')
                break
            
            # for 문을 돌면서 모든 클라이언트 들에게 동일한 메시지를 전송
            for conn in group :
                msg = 'Client' + str(recv[2]) + '>>' + str(recv[0])
                if recv[1] != conn : # client 본인이 보낸 메시지는 받을 필요가 없기 때문에 제외시킴
                    conn.send(bytes(msg.encode()))
                else : 
                    pass
            
        except :
            pass


def Recv(conn, count, send_queue) :
    print(f"RECV thread 시작 : {str(count)}번")

    while True :
        data = conn.recv(1024).decode()
        send_queue.put([data,conn,count])
        # 각각의 클라이언트의 메시지, 소켓정보, 쓰레드 번호를 send로 전송
    
# TCP echo server
# 에코서버 : 받은 메시지를 그대로 반환하는, 즉 print()하면 콘솔에 그대로 값이 나오는 것처럼 작동하는 서버
if __name__ == '__main__' :
# 파일을 직접 실행 시켰을 때만 작동하는 함수

    send_queue = Queue()
    # deque()과 Queue()의 차이점
    # queue는 멀티 스레드 환경에서 thread-safe 한 소통을 위해 만들어진 라이브러리
    # deque()는 자료구조의 일종 (container datatype). deque()가 작동속도는 더 빠르다.

    # 앞에서 반복사용한 서버 초기화
    HOST = ''
    PORT = 8080
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((HOST,PORT))
    server_socket.listen(10) # 한번에 접속 가능한 숫자 10개
    count = 0

    group = [] # 연결된 클라이언트의 소켓 정보를 리스트 형태로 저장

    while True :
        time.sleep(1)
        count = count + 1
        conn, addr = server_socket.accept()
        group.append(conn) # group에 클라이언트의 소켓 정보를 추가한다.
        print(f'Connected : {str(addr)}')

        # 소켓에 연결된 모든 클라이언트에게 동일한 메시지를 보내기 위한 쓰레드
        # 연결된 클라이언트가 1명 이상일 경우, 변경된 group 리스트를 반영한다.

        if count > 1 :
            send_queue.put('Group Changed')
            thread1 = threading.Thread(target=Send, args=(group,send_queue,))
            thread1.start()
            pass
        else :
            thraed1 = threading.Thread(target=Send, args=(group,send_queue,))
            thraed1.start()

        
        # 소켓에 연결된 각각의 클라이언트의 메시지를 받을 쓰레드
        thread2 = threading.Thread(target=Recv, args=(conn, count, send_queue,))
        thread2.start()
    
"""기능
1. 포트를 열고 클라이언트를 기다림
2. 클라이언트가 접속하면 count를 1 증가시키고, group이라는 리스트에 connection_socekt 정보를 담는다.
3. 만약 접속자가 1명 이상일 경우, 'Group Change'라는 메시지를 queue를 통해 send 쪽으로 보내고 종료시킨다.
4. Send 쓰레드가 생성되면 while 문을 돌며 Recv 쓰레드에서 queue를 통해 받은 메시지들 모든 클라이언트에게 보낸다. 단, 클라이언트 자신이 보낸 메시지는 받을 필요가 없으므로 conn정보를 비교하여 자신에게는 보내지 않도록 한다.
5. Recv쓰레드가 생성되면 while문을 돌며 메시지 받고 메시지를 보낸 상대의 conn정보와 메시지를 queue를 이용해 send로 보낸다.
"""