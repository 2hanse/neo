#!/usr/bin/env python

m = 0                       # 전역변수 m
n = 1

def func():
    m = 0                   # 지역 변수 m
    global n
    m += 1
    n += 1
    print(f'{m} vs {n}')
func()
print(m, n)                 # 전역 변수 m