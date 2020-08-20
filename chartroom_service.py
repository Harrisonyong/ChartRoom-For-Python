"""
    author:harrisonyong
    email:122023352@qq.com
    time:2020-08-20
    env:python3.6
    socket and epoll
"""
from socket import *
from select import *

HOST = "0.0.0.0"
POST = 8000
ADDR = (HOST, POST)

# 服务端套接字启动,采用epoll方法进行监听
sockfd = socket()
sockfd.setblocking(False)
sockfd.bind(ADDR)
sockfd.listen(5)
# epoll方法监听
ep = epoll()
ep.register(sockfd)
map = {sockfd.fileno():sockfd}
address = {}
name = {}
# 循环监听客户端连接进行处理
class Chart():
    def __init__(self,connfd):
        self.connfd = connfd

    def start(self):
        while True:
            data = self.connfd.recv(1024*10).decode()
            index = data.split(" ",1)[1]
            print(index)
            if index == "NAME":
                # self.connfd.send(b"ok")
                self.join()
            # self.connfd.send(b"Connect prepared")

    def join(self):



def main():
    # 循环监听触发事件
    while True:
        events = ep.poll()
        for fileno,event in events:
            # 判断连接事件
            if map[fileno] == sockfd:
                connfd,addre = sockfd.accept()
                print("connect is",addre)
                connfd.setblocking(False)
                ep.register(connfd)
                map[connfd.fileno()] = connfd
                address[connfd] = addre
            else:
                # 如果客户端连接,启动客户端处理类进行处理
                try:
                    Chart(map[fileno]).start()
                    g

                except BlockingIOError:
                    continue

if __name__ == '__main__':
    main()
