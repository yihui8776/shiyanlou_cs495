#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
Python 实现端口扫描器
'''

import sys

from socket import *

import thread

# portscan.py <host> <start_port>-<end_port>

def tcp_test(port):
    #创建socket，AF_INET指定使用IPv4协议,SOCK_STREAM:流式socket , for TCP
    sock = socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.settimeout(10)

    #参数为tuple，成功返回0，失败返回errno的值
    result = sock.connect_ex((target_ip,port))
    
    if result == 0:
        lock.acquire()
        print("Opened Port:", port)
        # 释放锁
        lock.release()

if __name__=='__main__':

    #主机名
    host  =  sys.argv[1]
    #端口
    portstrs = sys.argv[2].split('-')

    start_port = int(portstrs[0])

    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)

    #实例化一个锁
    lock = thread.allocate_lock()

    for port in range(start_port,end_port+1):
        #启动线程，参数为方法名和对应参数，参数是tuple
        thread.start_new_thread(tcp_test,(port,))
