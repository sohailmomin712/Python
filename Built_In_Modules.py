# modules can be considered same as code library
# in short nothing but the python file

# 1 math (used for performing mathematical operations)
import math
print(math.sqrt(4))
# output => 2.0

# 2 random(used for generating random numbers)
# random.randint() (random num generate krta hai)
# random.shuffle() (basically shuffles the iterables)

import random
randomNumber = random.randint(1,10)
print("Random generated number is",randomNumber)
# output => any random number from 1 to 10

import random
a = [1, 2, 3, 5]
random.shuffle(a)
print(a)
# output => shuffled numbers everytime

# 3 time
# time.ctime() shows current time at ur location
# time.sleep() adds the delay

import time
print(time.ctime())
# output => Sat Jul 25 13:01:33 2026

import time
print("Hello")
time.sleep(2) 
# this will add 2 seconds delay before executing the next line
print("World")

# 4 os module
# os.getcwd() gives current diirectory
# os.listdir() list krdeta hai apki directory ki files ko list kr deta hai

import os
print(os.getcwd())
# output => c:\Users\azim\Desktop\Python
print(os.listdir())
# output => ['Built_In_Functions.py', 'Built_In_Modules.py']