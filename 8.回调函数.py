#-*-coding:utf-8-*-
# Author:Lu Wei
import requests,time
from concurrent.futures import ThreadPoolExecutor

def get_page(url):
    res=requests.get(url)
    return {'url':url,'content':res.text}

def parserpage(ret):
    dic=ret.result()
    print(dic['url'])

start_time=time.time()
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
    # ret.add_done_callback(parserpage)
tp.shutdown()
for i in ret_l:
    parserpage(i)
print(time.time()-start_time)
