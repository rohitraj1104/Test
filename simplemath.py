#!/bin/bash
j=input("enter first value")
k=input("enter second value")


def sum(j,k):
  l= j+k
  print("TOTAL   " +str(l))

def expo(j,k):
   r=1
   o=0
   while o< k:
    r= j*r
    o += 1
   return r

sum(j,k)
print("exponent " +str(expo(j,k)))
