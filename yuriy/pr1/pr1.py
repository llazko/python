# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:26:37 2019

@author: lazko
"""

#%% Import section
#import sys
import turtle

#%% Routine section
def UP(length):
    direction = t.heading()
    dest = (360 - direction) % 360 + 90
    t.left(dest)
    t.forward(length)
    print("U: init direction = %s; destination = %s" %(direction, dest))
    pass
def DOWN(length):
    direction = t.heading()
    dest = (360 - direction) % 360 + 270
    t.left(dest)
    t.forward(length)
    print("D: init direction = %s; destination = %s" %(direction, dest))
    pass
def LEFT(length):
    direction = t.heading()
    dest = (360 - direction) % 360 + 180
    t.left(dest)
    t.forward(length)
    print("L: init direction = %s; destination = %s" %(direction, dest))
    pass
def RIGHT(length):
    direction = t.heading()
    dest = (360 - direction) % 360
    t.left(dest)
    t.forward(length)
    print("R: init direction = %s; destination = %s" %(direction, dest))
    pass

#%% Main section
print("Enter the drawind dirrective:")
#a=sys.stdin.readline()
a=input()
b=list(a)
print("It was entered: %s" %b)

t=turtle.Pen()
l=20 # length of element

print(t.heading())
for i in b:
    #print(i)
    if i == 'u' : UP(l)
    elif i == 'd' : DOWN(l)
    elif i == 'l' : LEFT(l)
    elif i == 'r' : RIGHT(l)
    elif i =='\n' : pass
    else : 
        print(i)
        print("Unallowed dirrective") 
    

input("Press ENTER to exit")



#sys.stdin.readline() # just waiting for something from key and then exit. to prevent automatic close of termial 
