import sys,os,time
import ConfigParser

class Config:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)
    def get(self, field, key):
        result = None
        try:
            result = self.cf.get(field, key)
        except:
            result = None
        return result
    def set(self, filed, key, value):
        try:
            self.cf.set(field, key, value)
            cf.write(open(self.path,'w'))
        except:
            return False
        return True

'''
config.ini format 
[baseconf]
mysql = mysql://buzz:123@localhost/buzz_master?option=open&charset=utf8&table=test
redis = redis://127.0.0.1:6379

[concurrent]
processor=20

'''
