#!/usr/bin/env python

sum = 0
for i in range(10):
    if i % 2 == 0:
        pass
    sum += i
    print(f'sum += {i}')
print()
print(f'sum = {sum}')


# pass : 아무것도 하지않음. 사용 : if, else에서 아무것도 하지 않는게 필요할때 사용