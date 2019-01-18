shiraz@shiraz-Vostro-1550:~$ cd Documents
shiraz@shiraz-Vostro-1550:~/Documents$ cd Python
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fh = open("input.txt","r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'input.txt'
>>> fh = open("input.txt","w")
>>> s="This is an input file"
>>> s="This is an input file".
  File "<stdin>", line 1
    s="This is an input file".
                             ^
SyntaxError: invalid syntax
>>> s="This is an input file."
>>> fh.write(s)
22
>>> s="This is an input file.\nProvide input to obtain desired output.\n\tinput1=integer\n\tinput2=string\n\tinput3==bool.\n"
>>> fh.writelines(s)
>>> fh.close
<built-in method close of _io.TextIOWrapper object at 0xb6c527ac>
>>> fh.flush
<built-in method flush of _io.TextIOWrapper object at 0xb6c527ac>
>>> fh = open("input.txt","r")
>>> 
>>> 
>>> fh.close()
>>> fh = open("input.txt","r")
>>> fh = open("input.txt","w")
>>> s="This is an input file.\nProvide input to obtain desired output.\n\tinput1=integer\n\tinput2=string\n\tinput3==bool.\n"
>>> fh.writelines(s)
>>> fh.write(s)
109
>>> fh.flush()
>>> fh.close()
>>> fh = open("input.txt","r")
>>> contents = fh.read()
>>> contents = fh.readline()
>>> contents
''
>>> f=open("gcd.py","r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'gcd.py'
>>> f=open("search.py","r")
>>> f.readline()
'def findpos(l,v):\n'
>>> 
>>> f.readline()
"    #return first position of 'v' in list\n"
>>> f.readline()
"    #return -1 if 'v' is not in the list\n"
>>> f.readline()
'    (found,i) = (False,0)\n'
>>> f.readline()
'    while i<len(l):\n'
>>> f.readline()
'        if not found and l[i]==v:\n'
>>> f.readline()
'            (found,pos) = (True,i)\n'
>>> f.readline()
'    if not found:\n'
>>> f.readline()
'        pos=-1\n'
>>> f.readline()
'    return(pos)\n'
>>> f.readline()
''
>>> f.readline()
''
>>> f.readline()
''
>>> f.close()
>>> f.readline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f=open("input.txt","r")
>>> f.readline()
'This is an input file.\n'
>>> f.readline()
'Provide input to obtain desired output.\n'
>>> f.readline()
'\tinput1=integer\n'
>>> f.readline()
'\tinput2=string\n'
>>> f.readline()
'\tinput3==bool.\n'
>>> f.readline()
'This is an input file.\n'
>>> f.readline()
'Provide input to obtain desired output.\n'
>>> f.readline()
'\tinput1=integer\n'
>>> f.readline()
'\tinput2=string\n'
>>> f.readline()
'\tinput3==bool.\n'
>>> f.readline()
''

Copying a file

shiraz@shiraz-Vostro-1550:~/Documents/Python$ rm input.txt
shiraz@shiraz-Vostro-1550:~/Documents/Python$ ls
binarySearch.py   mergesort.py  search.py         speed3.py  speed7.py
input.py          __pycache__   selectionSort.py  speed4.py  speed8.py
insertionSort.py  quicksort.py  speed1.py         speed5.py
isort.py          randomize.py  speed2.py         speed6.py
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fin=open("input.py","w")
>>> s="Input format
  File "<stdin>", line 1
    s="Input format
                  ^
SyntaxError: EOL while scanning string literal
>>> s="Input format\n userinput=input("take input from user")"
  File "<stdin>", line 1
    s="Input format\n userinput=input("take input from user")"
                                          ^
SyntaxError: invalid syntax
>>> s="input file"
>>> fin.write(s)
10
>>> l=list(range(1,50))
>>> fin.writelines(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: write() argument must be str, not int
>>> fin.write(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: write() argument must be str, not list
>>> s.flush()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'flush'
>>> fin.flush()
>>> fin.close()
>>> fin=open("input.py","r")
>>> fout=open("output.py","w")
>>> content=fin.readline()
>>> fout.writelines(content)
>>> fin.readline()
''
>>> fout.readline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> fin.close()
>>> fout.close()
>>> fin=open("input.py","r")
>>> fout=open("output.py","r")
>>> fin.readline()
'input file'
>>> fin.readline()
''
>>> fout.readline()
'input file'
>>> fout.readline()
''
>>> 


shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fin=open("input.py","a")
>>> s="\n input break \n"
>>> fin.write(s)
15
>>> fin.flush()
>>> fin.close()
>>> fin=open("input.py","r")
>>> for line in fin.readline():
...   print(line)
... 
i
n
p
u
t
 
f
i
l
e


>>> content=fin.readline()
>>> s=line.rstrip()
>>> for line in fin.readline():
...   print(line)
... 
>>> s
''
>>> content
' input break \n'
>>> text=fin.read()
>>> text
''
>>> fin.close()
>>> 




shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s="         hello"
>>> s
'\t\thello'
>>> t=l.strip()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> t=s.lstrip()
>>> t
'hello'
>>> p="
  File "<stdin>", line 1
    p="
      ^
SyntaxError: EOL while scanning string literal
>>> p="         I LOVE YOU            "
>>> t=p.strip()
>>> t
'I LOVE YOU'
>>> p="         I LOVE YOU            "
>>> t=p.rstrip()
>>> t
'\t\tI LOVE YOU'
>>> p.find("l")
-1
>>> p.find("L")
4
>>> s.find("l",3,len(s)
... )
4
>>> s
'\t\thello'
>>> s.find("l",4,len(s))
4
>>> s.find("l",5,len(s))
5
>>> t.find("l",4,len(s))
-1
>>> t
'\t\tI LOVE YOU'
>>> t.index()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: index() takes at least 1 argument (0 given)
>>> t.index(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'I' is not defined
>>> t.index("I")
2
>>> p.index("l")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> s
'\t\thello'
>>> t=s.lstrip()
>>> t
'hello'
>>> t.replace("ll","xt")
'hexto'
>>> t.replace("h","D")
'Dello'
>>> t.split("'")
['hello']
>>> t.split(":")
['hello']
>>> csvline="5,4,3,6,8"
>>> columns=csvline.split(",",2)
>>> columns
['5', '4', '3,6,8']
>>> columns=csvline.split(",")
>>> columns
['5', '4', '3', '6', '8']
>>> columns=csvline.split(",",2,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: split() takes at most 2 arguments (3 given)
>>> 
