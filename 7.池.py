#-*-coding:utf-8-*-
# Author:Lu Wei
import os
import time
import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# def func():
#     print('start',os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end',os.getpid())
#
# if __name__ == '__main__':
#     p=ProcessPoolExecutor(5)
#     for i in range(10):
#         p.submit(func)
#     p.shutdown()
#     print('main')

# 任务的参数 + 返回值
# def func(i,name):
#     print('start',os.getpid())
#     time.sleep(random.randint(1,3))
#     print('end',os.getpid())
#     return '%s * %s*%s'%(name,i,os.getpid())
#
# if __name__ == '__main__':
#     p=ProcessPoolExecutor(5)
#     p_l=[]
#     for i in range(3):
#         ret=p.submit(func,i,'luwei')
#         p_l.append(ret)
#     p.shutdown()
#     for i in p_l:
#         print(i.result())   #同步阻塞
#     print('main')


def func(i):
    print('start',os.getpid())
    time.sleep(random.randint(1,3))
    print('end',os.getpid())
    return '%s **%s'%(i,os.getpid())

if __name__ == '__main__':
    p=ThreadPoolExecutor(10)
    ret=p.map(func,range(10))
    for i in ret:
        print(i)
    # p_l=[]
    # for i in range(3):
    #     ret=p.submit(func,i,'luwei')
    #     p_l.append(ret)
    # p.shutdown()
    # for i in p_l:
    #     print(i.result())   #同步阻塞
    print('main')
