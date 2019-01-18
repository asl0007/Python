#Program to print position of n queens on a board

def addqueen(i,j,board):
  board['queen'][i]=j
  board['row'][i]=1
  board['col'][j]=1
  board['nwtose'][j-i]=1
  board['swtone'][j+i]=1

def free(i,j,board):
  return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)

def undoqueen(i,j,board):
  board['row'][i]=0
  board['col'][j]=0
  board['nwtose'][j-i]=0
  board['swtone'][j+i]=0


def printboard(board):
  for row in sorted(board['queen'].keys()):
    print((row,board['queen']['row']))

def initialize(board,n):
  for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
    board[key]={}
  for i in range(n):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][i]=0
  for i in range(-(n-1),n):
    board['nwtose'][i]=0
  for i in range(2*(n-1)):
    board['swtone'][i]=0

def placequeen(i,board):
  n=len(board['queen'].keys())
  for j in range(n):
    if free(i,j,board):
      addqueen(i,j,board)
      if i==n-1:
        return(True)
      else:
        extendsol = placequeen(i+1,board)
      if extendsol:
        return(True)
      else:
        undoqueen(i,j,board)
  else:
    return(False)

board={}
n=int(input("How many queens?"))
initialize(board,n)
if placequeen(0,board):
  printboard(board)

  
#Output

'''
shiraz@shiraz-Vostro-1550:~/Documents$ cd Python
shiraz@shiraz-Vostro-1550:~/Documents/Python$ ls
binarySearch.py   mergesort.py  quicksort.py      speed1.py  speed5.py
input.py          nqueen.py     randomize.py      speed2.py  speed6.py
insertionSort.py  output.py     search.py         speed3.py  speed7.py
isort.py          __pycache__   selectionSort.py  speed4.py  speed8.py
shiraz@shiraz-Vostro-1550:~/Documents/Python$ nano nqueen.py
shiraz@shiraz-Vostro-1550:~/Documents/Python$ more nqueen.py
def addqueen(i,j,board):
  board['queen'][i]=j
  board['row'][i]=1
  board['col'][j]=1
  board['nwtose'][j-i]=1
  board['swtone'][j+i]=1

def free(i,j,board):
  return(board['row'][i]===0 and board['col'][j]==0 and board['nwtose'][j-i]==0 
and board['swtone'][j+i]==0)

def undoqueen(i,j,board):
  board['row'][i]=0
  board['col'][j]=0
  board['nwtose'][j-i]=0
  board['swtone'][j+i]=0


def printboard(board);
  for row in sorted(board['queen'].keys()):
    print((row,board['queen']['row']))

def initialize(board,n):
  for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
    board[key]={}
  for i in range(n):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][i]0
  for i in range(-(n-1),n):
    board['nwtose'][i]=0
  for i in range(2*(n-1)):
    board['swtone'][i]=0

def placequeen(i,board):
  n=len(board['queen'].keys())
  for j in range n:
    if free(i,j,board):
      addqueen(i,j,board)
      if i==n-1:
        return(True)
      else:
        extendsol = placequeen(i+1,board)
      if extendsol:
        return(True)
      else:
        undoqueen(i,j,board)
  else:
    return(False)

board={}
n=int(input("How many queens?"))
initialize(board,n)
if placequeen(0,board):
  printboard(board)
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
  File "nqueen.py", line 9
    return(board['row'][i]===0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)
                            ^
SyntaxError: invalid syntax
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
  File "nqueen.py", line 18
    def printboard(board);
                         ^
SyntaxError: invalid syntax
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
  File "nqueen.py", line 28
    board['col'][i]0
                   ^
SyntaxError: invalid syntax
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
  File "nqueen.py", line 36
    for j in range n:
                   ^
SyntaxError: invalid syntax
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
How many queens?4
Traceback (most recent call last):
  File "nqueen.py", line 54, in <module>
    printboard(board)
  File "nqueen.py", line 20, in printboard
    print((row,board['queen']['row']))
KeyError: 'row'
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
How many queens?4
(0, 1)
(1, 3)
(2, 0)
(3, 2)
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3 nqueen.py
How many queens?8
(0, 0)
(1, 4)
(2, 7)
(3, 5)
(4, 2)
(5, 6)
(6, 1)
(7, 3)
shiraz@shiraz-Vostro-1550:~/Documents/Python$ 

'''
