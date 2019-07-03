#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import subprocess
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

IP_list=[]

# C段测试
def get_ip_list(net_segment):
    # 创建一个队列
    IP_QUEUE = Queue()
    list_segment = net_segment.split('.')
    ip_index = 0
    # 将需要 ping 的 ip 加入队列
    for i in range(1, 254):
        list_segment[-1] = str(ip_index + i)
        addr = ('.').join(list_segment)
        IP_QUEUE.put(addr)

    # 创建一个最大任务为100的线程池
    pool = ThreadPoolExecutor(max_workers=100)
    start_time = time.time()
    all_task = []
    while not IP_QUEUE.empty():
        all_task.append(pool.submit(ping_ip, IP_QUEUE.get()))

    # 等待所有任务结束
    wait(all_task, return_when=ALL_COMPLETED)
    return IP_list
    print('ping耗时：%s' % (time.time() - start_time)+"秒")

    # 定义一个执行 ping 的函数
def ping_ip(ip):
        res = subprocess.call('ping -n 2 -w 5 %s' % ip, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        if res == 0 :
            #print(ip + "存活")
            IP_list.append(ip)

if __name__ == '__main__':
    iplist= get_ip_list("192.168.1.0")  #C段
