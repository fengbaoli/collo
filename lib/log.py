# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  os

class Collectlog:
    def getfile_count(self,configfile,path):
        filecount_name={}
        self.path = path
        self.configfile = configfile
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                file = open(self.configfile,"a")
                #count = len(open(root+"/"+filename,'rU').readlines())
                counts = 1 
                context=root+":"+filename+":"+str(counts)+"\n"
                file.write(context)
            file.close()

    def readconfig(self,configfile):
        self.configfile = configfile
        file = open(self.configfile)
        for t in file.readlines():
            contents = t.strip().split(':')
            filepath=contents[0]
            filename=contents[1]
            counts =contents[2]
            print(filepath+"?"+filename+"?"+counts)
        file.close()

    def gencounts(self,configfile,filepath,filename,counts):
        self.configfile = configfile
        self.counts = counts
        self.filepath = filepath
        self.filename = filename 
        file = open(self.configfile)
        for t in file.readlines():
            tmpconffile= open("tmpconf.txt","a")
            newcontents=self.filepath+":"+self.filename+":"+str(self.counts)+"\n"
            tmpconffile.write(newcontents)
            tmpconffile.close()
        file.close()
