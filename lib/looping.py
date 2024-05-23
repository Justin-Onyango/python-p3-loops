#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    sec = 10
    while sec > 0:
        print(sec)
        sec -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [num ** 2 for num in int_list]

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))


def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
