#!/usr/bin/env python

import random

def findMax(data):
    max = data[0]
    for i in range(len(data)):         # 반복 횟수를 알기 때문에 for문을 사용
        if data[i] > max:
            max = data[i]
    return max

data = random.sample(range(1,101), 10)
print(data)
print(f'Max value is : {findMax(data)}')