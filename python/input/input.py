#!/usr/bin/env python

n = int(input("How much number input? :"))

building = list(map(int, input().split()))
print("\nbulding : ", building)

mid_building = min(building)
print("\nmin(building) : ", mid_build)

min_build = min(building) * n
print("\nmin(building) * n : ", min_build_n)

sum_building = sum(building)
print("\nsum(building) : ", sum_building)

result = sum_building - min_build_n
print("\nsum(building) - (min(building) * n) : ", result)
