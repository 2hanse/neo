#!/usr/bin/env python

from prime_func import is_prime

while True:
    try:
        num = int(input("input number(0 : quit): "))
        if num == 0:
            break
        if is_prime(num):
            print(f"{num} is prime number")
        else:
            print(f"{num} is not prime number")
    except ValueError:
        print("Please enter a valid integer.")
