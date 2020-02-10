### day35

#### 今日内容

- 锁
  - 为什么要用锁
  - 互斥锁
  - 使用互斥锁产生一个死锁现象
  - 递归锁
- 线程队列
  - queue
    - 先进先出
    - 后进先出
    - 优先级队列
- 池
  - 进程池、线程池

 线程即便有GIL，其实数据不安全。（先计算后赋值才容易出现数据不安全的问题）+=，-=，*=，/=



#### 1.互斥锁（rlock）

#互斥锁是锁中的一种，在同一个线程中，不能连续出现acquire多次。

![image-20200207192953719](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200207192953719.png)

 线程即便有GIL，其实数据不安全。（先计算后赋值才容易出现数据不安全的问题）+=，-=，*=，/=

​		

```
# 即便是线程 即便有GIL 也会出现数据不安全的问题
    # 1.操作的是全局变量
    # 2.做一下操作
        # += -= *= /+ 先计算再赋值才容易出现数据不安全的问题
        # 包括 lst[0] += 1  dic['key']-=1
#在步骤stroe_global前一步为完成运算结果，在store_global步骤时进行赋值存储。

from threading import Thread,Lock

a=0

def add_f(lock):
    global a
    for i in range(100000):
        with lock:
            a+=1

def sub_f(lock):
    global a
    for i in range(100000):
        with lock:
            a-=1
lock=Lock()
t1=Thread(target=add_f,args=(lock,))
t1.start()
t2=Thread(target=sub_f,args=(lock,))
t2.start()
t1.join()
t2.join()
print('--',a)#加锁会影响程序的执行效率，但是保证了数据的安全
```

#### 2.单实例

```
import time
from threading import Lock
from threading import Thread

class A:
    __instance=None
    lock=Lock()
    def __new__(cls, *args, **kwargs):
       with cls.lock:				#加锁来实现数据安全
        if not cls.__instance:
            time.sleep(0.1)			#由于sleep阻塞，该线程进入阻塞状态，空闲出cpu给其他线程使用
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
```



#### 3.死锁

```
import time
from threading import Thread,Lock
noodle_lock=Lock()
fork_lock=Lock()

def eat1(name,noodle_lock,fork_lock):
    noodle_lock.acquire()
    print('%s抢到面了'%name)
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.2)
    fork_lock.release()
    print('%s放下叉子了' % name)
    noodle_lock.release()
    print('%s放下面了' % name)

def eat2(name,noodle_lock,fork_lock):
    fork_lock.acquire()
    print('%s抢到叉了' % name)
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.2)
    noodle_lock.release()
    print('%s放下面了' % name)
    fork_lock.release()
    print('%s放下叉子了' % name)


lst = ['alex','wusir','taibai','yuan']
Thread(target=eat1,args=(lst[0],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[1],noodle_lock,fork_lock)).start()
Thread(target=eat1,args=(lst[2],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[3],noodle_lock,fork_lock)).start()
```

#### 4.Rlock

在一个线程中，可以连续acuquire多次不会被锁住，但是占用更多资源。

如果存在多把Rlock也会造成线程锁死的情况

```
from threading import Rlock，Thread
import time

fork_lock=noodle_lock=RLock()	#本质为只能有一把锁
#noodle_lock=RLock()
#fork_lock=RLock()

def eat1(name,noodle_lock,fork_lock):
    noodle_lock.acquire()
    print('%s抢到面了'%name)
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.2)
    fork_lock.release()
    print('%s放下叉子了' % name)
    noodle_lock.release()
    print('%s放下面了' % name)

def eat2(name,noodle_lock,fork_lock):
    fork_lock.acquire()
    print('%s抢到叉了' % name)
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    print('%s吃了一口面'%name)
    time.sleep(0.2)
    noodle_lock.release()
    print('%s放下面了' % name)
    fork_lock.release()
    print('%s放下叉子了' % name)



lst = ['alex','wusir','taibai','yuan']
Thread(target=eat1,args=(lst[0],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[1],noodle_lock,fork_lock)).start()
Thread(target=eat1,args=(lst[2],noodle_lock,fork_lock)).start()
Thread(target=eat2,args=(lst[3],noodle_lock,fork_lock)).start()

```



5.互斥锁解决死锁方法

```
#1.修改代码逻辑
#2.
```





#### 6.队列

##### 6.1Queue（先进先出队列）

```
from queue import Queue
#Queue 先进先出队列
q=Queue()
q.put(1)
q.put(2)
q.put(3)#如果Queue（n）队列设置队列的深度，那put超过该深度的时候，进程就会一直卡着。q.put_nowait()表示不等待如果队列满了直接报错

print(q.get())
print(q.get())
print(q.get())#当队列为空时，那get会将进程一直卡着，get_nowait()表示不等待，进程直接报错

注意，queue队列的报错 在报错是如果希望用try方法则需要import queue才能找到对应错误类型
```

##### 6.2LifoQueue（后进先出队列） 

```
#栈
from queue import LifoQueue
q=LifoQueue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())
```

##### 6.3PriorityQueue（优先级队列）

```
#数值越小，优先级越大
from queue import PriorityQueue
q=PriorityQueue()
q.put((10,'luwei'))
q.put((5,'yaoting'))
q.put((15,'ting'))

print(q.get())
print(q.get())
print(q.get())
```



```
# 先进先出
    # 写一个server，所有的用户的请求放在队列里
        # 先来先服务的思想
# 后进先出
    # 算法
# 优先级队列
    # 自动的排序
    # 抢票的用户级别 100000 100001
    # 告警级别
```



#### 7.池

```
# 为什么要有池？concurrent.futures
    # 预先的开启固定个数的进程数，当任务来临的时候，直接提交给已经开好的进程
    # 让这个进程去执行就可以了
    # 节省了进程，线程的开启 关闭 切换都需要时间
    # 并且减轻了操作系统调度的负担
```

```
# ThreadPoolExcutor
# ProcessPoolExcutor

# 创建一个池子
# tp = ThreadPoolExcutor(池中线程/进程的个数)
# 异步提交任务
# ret = tp.submit(函数,参数1，参数2....)
# 获取返回值
# ret.result()
# 在异步的执行完所有任务之后，主线程/主进程才开始执行的代码
# tp.shutdown() 阻塞 直到所有的任务都执行完毕
# map方法
# ret = tp.map(func,iterable) 迭代获取iterable中的内容，作为func的参数，让子线程来执行对应的任务
# for i in ret: 每一个都是任务的返回值
# 回调函数
# ret.add_done_callback(函数名)
# 要在ret对应的任务执行完毕之后，直接继续执行add_done_callback绑定的函数中的内容，并且ret的结果会作为参数返回给绑定的函数
```



##### 7.1进程池

```
import os
import time
import random
from concurrent.futures import ProcessPoolExecutor

def func():
    print('start',os.getpid())
    time.sleep(random.randint(1,3))
    print('end',os.getpid())

if __name__ == '__main__':
    p=ProcessPoolExecutor(5)	#生成一个进程池，进程数为5，一般进程数是CPU+1
    for i in range(10):
        p.submit(func)		   #将任务提交至进程池中
    p.shutdown()			   #关闭进程池之后就不能再向进程池提交任务，并且会阻塞，直到已经提交的任务全部执行完成
    print('main')

```

```
# 任务的参数 + 返回值
def func(i,name):
    print('start',os.getpid())
    time.sleep(random.randint(1,3))
    print('end',os.getpid())
    return '%s * %s*%s'%(name,i,os.getpid())

if __name__ == '__main__':
    p=ProcessPoolExecutor(5)
    p_l=[]
    for i in range(3):
        ret=p.submit(func,i,'luwei')		#传参数需要args元组，因为submit方法本身接收*args，**kwargs
        p_l.append(ret)
    p.shutdown()
    for i in p_l:
        print(i.result())   #同步阻塞
    print('main')
```



##### 7.2线程池

```
import os
import time
import random
from concurrent.futures import ThreadPoolExecutor
def func(i,name):
    print('start',os.getpid())
    time.sleep(random.randint(1,3))
    print('end',os.getpid())
    return '%s * %s*%s'%(name,i,os.getpid())

if __name__ == '__main__':
    p=ThreadPoolExecutor(5)
    #ret=p.map(func,range(10))		#map方法只能传一个参数
    #for i in ret:
    #    print(i)
    p_l=[]
    for i in range(3):
        ret=p.submit(func,i,'luwei')
        p_l.append(ret)
    p.shutdown()
    for i in p_l:
        print(i.result())   #同步阻塞
    print('main')
```

#### 8.回调函数



```
import requests
from concurrent.futures import ThreadPoolExecutor

def get_page(url):
    res=requests.get(url)
    return {'url':url,'content':res.text}	#返回值给相应线程池中的线程任务

def parserpage(ret):
    dic=ret.result()
    print(dic['url'])

tp=ThreadPoolExecutor(5)
url_lst = [
    'http://www.baidu.com',   # 3
    'http://www.cnblogs.com', # 1
    'http://www.douban.com',  # 1
    'http://www.tencent.com',
    'http://www.cnblogs.com/Eva-J/articles/8306047.html',
    'http://www.cnblogs.com/Eva-J/articles/7206498.html',
]
ret_l=[]

for url in url_lst:
    ret=tp.submit(get_page,url)
    ret_l.append(ret)
    # ret.add_done_callback(parserpage)  #回调函数，线程中谁先执行完成，则谁先调用下面函数
tp.shutdown()						#关闭线程池
for i in ret_l:			#线程池都执行完成之后，再去取内容
    parserpage(i)
```

