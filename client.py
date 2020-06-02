import json
import socket
import threading
from datetime import datetime

host_port = ('127.0.0.1', 8888)

s = socket.socket()
s.connect(host_port)
print(f'连接{host_port}成功！')
true = True


def recv(so):
    global true
    while true:
        data = json.loads(so.recv(1024).decode())
        if data == 'quit':
            true = False
        print(f'来自对方的消息 : {data[1]}', data[0])


thread1 = threading.Thread(target=recv, args=(s, ))
thread1.start()

while true:
    msg = input()
    msg = json.dumps([msg, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    s.send(msg.encode())
    if msg == 'quit':
        true = False

s.close()