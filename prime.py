# Program to check whether the no is prime or not

def isPrime(n):
    flag=1
    if(n==0 or n==1):
        flag=0
    for j in range(2,int(sqrt(n))+1):
        if(n%j == 0):
            flag=0
    return flag
  
  
