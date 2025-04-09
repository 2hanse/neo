#!/usr/bin/env python

def division_function(a, b):
    try:
        print(a/b)
    except TypeError as e:      #exception이 훨씬 큰 개념이라 first만 출력됨.
        print('First')
    except TypeError as e:
        print('Second')
    except ZeroDivisionError as e:
        print('Third')

division_function("a", 1)
division_function(1, 0)
division_function(4, 2)