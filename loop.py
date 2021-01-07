#////Factors using for loop////

def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist = flist + [i]
    return(flist)


#>>> from loop import *
#>>> factors(98)
#[1, 2, 7, 14, 49, 98]
#>>> factors(10)
#[1, 2, 5, 10]



#////Factors using while loop in reverse order////

def factors(n):
    flist=[]
    i=n
    while i>0:
        if n%i==0:
            flist = flist + [i]
        i=i-1
    return(flist)


#>>> from loop import *
#>>> factors(98)
#[98, 49, 14, 7, 2, 1]
#>>> factors(10)
#[10, 5, 2, 1]




#////POWER OF A NUMBER  //// i.e x raise to the power n

def power(x,n):
    ans=1
    for i in range(0,n):
        ans = ans * x
    return(ans)


#>>> from loop import *
#>>> power(2,3)
#8
#>>> power(3,9)
#19683
#>>> power(5,5
#... )
#3125



#  UPDATE a list 'l' at position 'i' with value 'v'

def update(l,i,v):
    if i>0 and i<len(l):
        l[i]=v
        return(True)
    else:
        v=v+1
        return(False)
    
    
  
#>>> l = list(range(1,9))
#>>> l = [0] + l
#>>> l = l + [9]
#>>> l
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#>>> from loop import *
#>>> update(l,4,9)
#True
#>>> l
#[0, 1, 2, 3, 9, 5, 6, 7, 8, 9]
#>>> update(l,5,0)
#True
#>>> update(l,9,0)
#True
#>>> update(l,19,0)
#False
#>>> l
#[0, 1, 2, 3, 9, 0, 6, 7, 8, 0]

#RECURSIVE FUNCTION

def factorial(n):
    if n<=0:
        return(1)
    else:
        val = n * factorial(n-1)
        return(val)
    
   
#>>> from loop import *
#>>> factorial(5)
#120
#>>> factorial(10)
#3628800
#>>> factorial(7)
#5040

 
def isPrime(n):
    return(factors(n)==[1,n])

#>>> from loop import *
#>>> isPrime(3)
#True
#>>> 


def primeUpto(n):
    primelist=[]
    for i in range(1,n+1):
        if isPrime(i):
            primelist = primelist + [i]
    return(primelist)

#>>> from loop import *
#>>> primeUpto(100)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#>>> primeUpto(50)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#>>>


def nprime(n):
    (count,i,plist)=(0,1,[])
    while count<n:
        if isPrime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1
    return(plist)

>>> from loop import *
>>> nprime(5)
[2, 3, 5, 7, 11]
>>> nprime(10)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Problem link - https://www.hackerrank.com/challenges/30-loops/problem
# Solution
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print(str(n) + " x " + str(i) + " = " + str(n*i))
