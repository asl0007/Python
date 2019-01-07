def insertionSort(seq):
    for sliceEnd in range(len(seq)):
        '''Build longer and longer sorted slices
           In each iteration seq[0:sliceEnd] already sorted
           Move first element after sorted slice left till 
           it is in the correct place'''
        pos = sliceEnd
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos - 1

            
            
            
  '''
  
>>> from insertionSort import *
>>> l=[8,54,87,9,43,2,9]
>>> insertionSort(l)
>>> l
[2, 8, 9, 9, 43, 54, 87]
>>> 

  '''
