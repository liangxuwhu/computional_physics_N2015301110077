#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:39:38 2017

@author: lxwhu
"""

x = int(input('input a number:'))
for i in range(x):
    print(i*' '+'#      #       #')
    print(i*' '+'#        #   #')
    print(i*' '+'#          #  ')
    print(i*' '+'#        #   #')
    print(i*' '+'####   #       #')
    if i==x-1:
        break
    import time
    time.sleep(0.5)
    import os
    i=os.system('cls')