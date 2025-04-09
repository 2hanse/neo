#!/usr/bin/env python

i = input("Enter a number: ")
j = input("Enter another number: ")

a = lambda i, j : i + j
print(f'{i} + {j} = {a(int(i), int(j))}')

# 하잖은걸 시킬때 사용.