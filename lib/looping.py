#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    return [x ** 2 for x in int_list]

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            if i % 3 == 0:
              print("Fizz")
            else:
                if i % 5 == 0:
                  print("Buzz")
                else:
                  print(i)