def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)#current position in a,b

    while i+j < m+n:#i+j is no of elements sorted so far

        if i==m:#'a[]' is empty,add 'b[]' to 'c[]'
            c.append(b[j])
            j=j+1

        elif j==n:#'b[]' is empty,add 'a[]' to 'c[]'
            c.append(a[i])
            i=i+1

        elif a[i]<=b[j]:#head of 'a[]' is smaller
            c.append(a[i])
            i=i+1

        elif a[i]>b[j]:#head of 'b[]' is smaller
            c.append(b[j])
            j=j+1

    return(c)


def mergesort(a,l,r):
    #sort the slice a[left:right]

    if r-l <= 1:#Base case
        return(a[l:r])

    if r-l > 1:#recursive call

        mid=(l+r)//2
        left=mergesort(a,l,mid)
        right=mergesort(a,mid,r)

        return(merge(left,right))
    

'''
shiraz@shiraz-Vostro-1550:~$ cd Documents
shiraz@shiraz-Vostro-1550:~/Documents$ cd Python
shiraz@shiraz-Vostro-1550:~/Documents/Python$ ls
binarySearch.py   mergesort.py  selectionSort.py  speed3.py  speed6.py
insertionSort.py  __pycache__   speed1.py         speed4.py  speed7.py
isort.py          search.py     speed2.py         speed5.py  speed8.py
shiraz@shiraz-Vostro-1550:~/Documents/Python$ more mergesort.py
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)#current position in a,b

    while i+j < m+n:#i+j is no of elements sorted so far

        if i==m:#'a[]' is empty,add 'b[]' to 'c[]'
            c.append(b[j])
            j=j+1

        elif j==n:#'b[]' is empty,add 'a[]' to 'c[]'
            c.append(a[i])
            i=i+1

        elif a[i]<=b[j]:#head of 'a[]' is smaller
            c.append(a[i])
            i=i+1

        elif a[i]>b[j]:#head of 'b[]' is smaller
            c.append(b[j])
            j=j+1

    return(c)


def mergesort(a,l,r):
    #sort the slice a[left:right]

    if r-l <= 1:#Base case
        return(a[l:r])

    if r-l > 1:#recursive call

        mid=(l+r)//2
        left=mergesort(a,l,mid)
        right=mergesort(a,mid,r)

        return(merge(left,right)
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shiraz/Documents/Python/mergesort.py", line 38
    return(merge(left,right)
                           ^
SyntaxError: unexpected EOF while parsing
>>> from mergesort import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shiraz/Documents/Python/mergesort.py", line 38
    return(merge(left,right)        
                                   ^
SyntaxError: unexpected EOF while parsing
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shiraz/Documents/Python/mergesort.py", line 38
    return(merge(left,right)        
                                   ^
SyntaxError: unexpected EOF while parsing
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shiraz/Documents/Python/mergesort.py", line 37
    return(merge(left,right)        
                                   ^
SyntaxError: unexpected EOF while parsing
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shiraz/Documents/Python/mergesort.py", line 38
    return(merge(left,right)        
                                   ^
SyntaxError: unexpected EOF while parsing
>>> from mergesort import *
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
>>> a=list(range(10,100,5)
... )
>>> a
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> b=list(range(2,101,3))
>>> b
[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
>>> merge(a,b)
[2, 5, 8, 10, 11, 14, 15, 17, 20, 20, 23, 25, 26, 29, 30, 32, 35, 35, 38, 40, 41, 44, 45, 47, 50, 50, 53, 55, 56, 59, 60, 62, 65, 65, 68, 70, 71, 74, 75, 77, 80, 80, 83, 85, 86, 89, 90, 92, 95, 95, 98]
>>> c=[4,8,45,76,43,98,54,9,54,32]
>>> c
[4, 8, 45, 76, 43, 98, 54, 9, 54, 32]
>>> mergesort(c,0,len(c))
[4, 8, 9, 32, 43, 45, 54, 54, 76, 98]
>>> l1=[1,2,3]
>>> l2=[3,2,3,5]
>>> l1
[1, 2, 3]
>>> l2
[3, 2, 3, 5]
>>> mergesort(l1,l2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: mergesort() missing 1 required positional argument: 'r'
>>> merge(l1,l2)
[1, 2, 3, 3, 2, 3, 5]
>>> mergesort(merge(l1,l2),0,len(merge(l1,l2)))
[1, 2, 2, 3, 3, 3, 5]
>>> list1= list(range(0,1000000,2) + list(range(1,1000000,2)
... )
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'range' and 'list'
>>> list1= list(range(0,1000000,2)) + list(range(1,1000000,2))
'''

'''
////UNION////
shiraz@shiraz-Vostro-1550:~/Documents/Python$ more mergesort.py
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)#current position in a,b

    while i+j < m+n:#i+j is no of elements sorted so far
                  
        if i==m:#'a[]' is empty,add 'b[]' to 'c[]'
            c.append(b[j])
            j=j+1

        elif j==n:#'b[]' is empty,add 'a[]' to 'c[]'
            c.append(a[i])
            i=i+1
                
        elif a[i]<=b[j]:#head of 'a[]' is smaller
            while a[i]==b[j]:
                j=j+1
            c.append(a[i])
            i=i+1

        elif a[i]>b[j]:#head of 'b[]' is smaller
            c.append(b[j])
            j=j+1

    return(c)


def mergesort(a,l,r):
    #sort the slice a[left:right]

    if r-l <= 1:#Base case
        return(a[l:r])

    if r-l > 1:#recursive call

        mid=(l+r)//2
        left=mergesort(a,l,mid)
        right=mergesort(a,mid,r)

        return(merge(left,right))        
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
>>> l1=[1,2,3]
>>> l2=[3,2,3,5]
>>> mergesort(merge(l1,l2),0,len(merge(l1,l2)))
[1, 2, 3, 5]
>>> 
'''

def union(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)#current position in a,b
    while i+j < m+n:#i+j is no of elements sorted so far

        if i==m:#'a[]' is empty,add 'b[]' to 'c[]'
            c.append(b[j])
            j=j+1

        elif j==n:#'b[]' is empty,add 'a[]' to 'c[]'
            c.append(a[i])
            i=i+1

        elif a[i]<=b[j]:#head of 'a[]' is smaller
            while a[i]==b[j]:
                j=j+1
            c.append(a[i])
            i=i+1

        elif a[i]>b[j]:#head of 'b[]' is smaller
            c.append(b[j])
            j=j+1

    return(c)

'''
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mergesort import *
>>> l=[1,5,3,4,2,0,8,7,9]
>>> mergesort(l,0,len(l))
[0, 1, 2, 3, 4, 5, 7, 8, 9]
>>> a=[1,2,3,4,32,54,67]
>>> union(l,a)
[1, 2, 3, 4, 5, 3, 4, 2, 0, 8, 7, 9, 32, 54, 67]
>>> union(a,l)
[1, 2, 3, 4, 5, 3, 4, 2, 0, 8, 7, 9, 32, 54, 67]
>>> l=mergesort(l,0,len(l))
>>> l
[0, 1, 2, 3, 4, 5, 7, 8, 9]
>>> union(a,l)
[0, 1, 2, 3, 4, 5, 7, 8, 9, 32, 54, 67]
>>> union(l,a)
[0, 1, 2, 3, 4, 5, 7, 8, 9, 32, 54, 67]
'''


