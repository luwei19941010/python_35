#-*-coding:utf-8-*-
# Author:Lu Wei
import time
from threading import Lock
from threading import Thread

class A:
    __instance=None
    lock=Lock()
    def __new__(cls, *args, **kwargs):
        #with cls.lock:
        if not cls.__instance:
            time.sleep(0.1)
            cls.__instance=super().__new__(cls)
        return cls.__instance
    def __init__(self,name,age):
        self.name=name
        self.age=age

def func():
    a=A('luwei',50)
    print(a)

for i in range(10):
    t=Thread(target=func)
    t.start()
