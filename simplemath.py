#!/bin/bash
j=input("enter first value==")
k=input("enter second value==")


def sum(j,k): #this is to add two number
  l= j+k
  print("\nTOTAL   " +str(l))

def expo(j,k):  #this is a exponential function 
   r=1
   o=0
   while o< k:
    r= j*r
    o += 1
   return r

def multiple(n,m):
  if n and m== False:
   print("are u stupid")
  else:
   mul=n*m
  return mul


sum(j,k)
print("\nexponent== " +str(expo(j,k)))
print("\nmultiply of two number== " +str(multiple(j,k)) + "\n")
