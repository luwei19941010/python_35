#-*-coding:utf-8-*-
# Author:Lu Wei
import time
from threading import RLock,Thread

# rlock=RLock()
# rlock.acquire()
# print('*'*20)
# rlock.acquire()
# print('-'*20)
# rlock.release()
# rlock.release()

fork_lock=noodle_lock=RLock()


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
