# -*- coding:utf-8 -*-
__author__ = 'blfeng'

from socket import *
import os
import struct
import time
import linecache
class Sendlog:
    def slog(self,ip,port,filename,old_counts,now_counts):
        self.port = port
        self.ip = ip
        self.filename = filename
        self.old_counts = int(old_counts)
        self.now_counts = int(now_counts)
        ADDR = (self.ip,self.port)
        BUFSIZE = 1024 
        FILEINFO_SIZE=struct.calcsize('128s32sI8s')
        sendSock = socket(AF_INET,SOCK_STREAM,0)
        sendSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sendSock.connect(ADDR)
        fhead=struct.pack('128s11I',self.filename,0,0,0,0,0,0,0,0,os.stat(self.filename).st_size,0,0)
        sendSock.send(fhead) 
        tmpdata = linecache.getlines(self.filename)[self.old_counts-1:self.now_counts]
        tmpfile = open("tmpdata.tmp","a")
        for data in tmpdata:
            tmpfile.write(data)
        tmpfile.close()
        linecache.clearcache()
        fp = open("tmpdata.tmp",'rb')
        while 1:
           filedata = fp.read(BUFSIZE)
           if not filedata: break
           sendSock.send(filedata)
        print "文件传送完毕，正在断开连接..."
        fp.close()
        os.remove("tmpdata.tmp")
        sendSock.close()
        print "连接已关闭..."
        time.sleep(10)
