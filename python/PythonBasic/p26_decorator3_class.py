#!/usr/bin/env python

import datetime

class DatetimeDecorator:
    def __init__(self, f):  # f : 이 클래스가 호출되면서 받아내는 파라미터. ,, 그 파라미터를 self의 f로 정의
        self.func = f
    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())
        print()

class MainClass:
    @DatetimeDecorator
    def func1():
        print("Main Function1 start")

    @DatetimeDecorator
    def func2():
        print("Main Function2 start")

    @DatetimeDecorator
    def func3():
        print("Main Function3 start")

my = MainClass()
my.func1()
my.func2()
my.func3()