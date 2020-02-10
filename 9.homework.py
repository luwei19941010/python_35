#-*-coding:utf-8-*-
# Author:Lu Wei
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests,time,random

#使用线程实现
# def get_page(url,list):
#     res=requests.get(url)
#     list.append(res.text)
#
# def w_page(list):
#     with open('url',mode='w',encoding='utf-8') as f:
#         for i in list:
#             f.write(i)
#
# if __name__ == '__main__':
#     url='http://www.baidu.com'
#     tp_l=[]
#     tp=Thread(target=get_page,args=(url,tp_l))
#     tp.start()
#     tp.join()
#     tp2 = Thread(target=w_page, args=(tp_l))
#     tp2.start()
#     tp2.join()

#使用线程池
# from concurrent.futures import ThreadPoolExecutor
#
# def get_page(url):
#     res=requests.get(url)
#     return res.text
#
# def del_page(ret):
#     with open('url1',mode='a',encoding='utf-8') as f:
#         f.write(ret.result())
#
# if __name__ == '__main__':
#     url_lst = [
#         'http://www.baidu.com',  # 3
#         'http://www.cnblogs.com',  # 1
#         'http://www.douban.com',  # 1
#         'http://www.tencent.com',
#         'http://www.cnblogs.com/Eva-J/articles/8306047.html',
#         'http://www.cnblogs.com/Eva-J/articles/7206498.html',
#     ]
#     tp=ThreadPoolExecutor(5)
#     for url in url_lst:
#         ret=tp.submit(get_page,url)
#         ret.add_done_callback(del_page)
#     tp.shutdown()

# def func1():
#     print('func1')
#     time.sleep(1)
#     tp1=Thread(target=func2)
#     tp1.start()
#     tp1.join()
#     tp=Thread(target=func3)
#     tp.start()
#     tp.join()
#
#
#
# def func2():
#     print('func2')
#
# def func3():
#     print('func3')

#
# if __name__ == '__main__':
#     p1=Process(target=func1)
#     p1.start()
#     p1.join()
#     p2=Process(target=func2)
#     p2.start()
#     p2.join()

def func1(a):
    print('stat func1',a)
    time.sleep(random.random())
    tp=ThreadPoolExecutor(10)
    for i in range(20):
        tp.submit(func2,i)
    print('end','func1',a)


def func2(i):
    print('stats func2',i)
    time.sleep(1)
    print('end func2',i)


if __name__ == '__main__':
    p=ProcessPoolExecutor(5)
    for i in range(5):
        p.submit(func1,i)