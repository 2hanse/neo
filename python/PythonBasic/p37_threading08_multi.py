#!/usr/bin/env python

import threading, queue, time

data = 0

def generator(start, end):
    global data
    for _ in range(start, end + 1):
        buf = data
        time.sleep(0.01)
        data = buf + 1

t1 = threading.Thread(target=generator, args=(1,10))
t2 = threading.Thread(target=generator, args=(1,10))

t1.start()
t2.start()

t1.join()
t2.join()

print(data)    # data 값이 t1인지 t2인지 어떤 값인지 알 수 없음,, 순차적으로 실행하는게 아니기 때문.