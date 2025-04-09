#!/usr/bin/env python

from minimum import min                  # from import : 내부에 있는것을 가져다 쓰는 느낌

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print(f'Min Number is {min(a,b)}')