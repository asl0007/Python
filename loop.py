#////Factors using for loop////

def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist = flist + [i]
    return(flist)

<!--
#>>> from loop import *
#>>> factors(98)
#[1, 2, 7, 14, 49, 98]
#>>> factors(10)
#[1, 2, 5, 10]
-->


#////Factors using while loop in reverse order////

def factors(n):
    flist=[]
    i=n
    while i>0:
        if n%i==0:
            flist = flist + [i]
        i=i-1
    return(flist)

<!--
#>>> from loop import *
#>>> factors(98)
#[98, 49, 14, 7, 2, 1]
#>>> factors(10)
#[10, 5, 2, 1]
-->
