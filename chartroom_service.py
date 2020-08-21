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
usr = {}
# 循环监听客户端连接进行处理
class Chart():
    def __init__(self,connfd,addre,name = None):
        self.connfd = connfd
        self.addre = addre
        self.name = name

    def join(self,index):
        if index[0] == "NAME":
            for n in usr.values():
                if n.name == index[1]:
                    self.connfd.send(b"Fail")
                    return
            else:
                self.name = index[1]
                self.connfd.send(b"ok")

    def start(self):
        while True:
            data = self.connfd.recv(1024*10).decode()
            index = data.split(" ",1)
            print(index)
            self.join(index)


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
                # 存储连接客户端对象,对象中包含客户端信息和客户端使用方法
                usr[connfd.fileno()] = Chart(connfd,addre)
            else:
                # 如果客户端连接,启动客户端处理类进行处理
                try:
                    usr[fileno].start()
                except BlockingIOError:
                    continue

if __name__ == '__main__':
    main()
