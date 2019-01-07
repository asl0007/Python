def SelectionSort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        (l[start],l[minpos]) = (l[minpos],l[start])     

        
'''        
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from selectionSort import *
>>> l=[8,54,87,9,43,2,9]
>>> SelectionSort(l)
>>> l
[2, 8, 9, 9, 43, 54, 87]
>>> 
'''
