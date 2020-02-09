#-*-coding:utf-8-*-
# Author:Lu Wei
#
# from threading import Thread,Lock
#
# a=0
#
# def add_f(lock):
#     global a
#     for i in range(100000):
#         with lock:
#             a+=1
#
# def sub_f(lock):
#     global a
#     for i in range(100000):
#         with lock:
#             a-=1
# lock=Lock()
# t1=Thread(target=add_f,args=(lock,))
# t1.start()
# t2=Thread(target=sub_f,args=(lock,))
# t2.start()
# t1.join()
# t2.join()
# print('--',a)

from threading import Lock
lock = Lock()
lock.acquire()
print('*'*20)
lock.release()
lock.acquire()
print('-'*20)
lock.release()