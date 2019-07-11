#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:26:41 2019

@author: bhumika
"""
print("welcome to liar's poker")
print ("Your bill")

mylist = []
complist = []
import random

def roll(x):
    for i in range(8):
        f = random.randint(0,9)
        x.append(f)
    
roll(mylist)
roll(complist)

print(mylist)
b = int(input("What's your bid? enter number of digit(s) you want to bid "))
c = int(input("Enter the digit that you are bidding "))

d = complist.count(c)

if b <= 3:
    print("i bid")
else:
    if d + 3 > b:
        print("I bid")
    else:
        print("challenge")
        print("My bill", complist)
    
if d + mylist.count(c) < b:
    print("I win")
else:
    print("I lose!")
    
