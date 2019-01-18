shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> score["test1"]={}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'score' is not defined
>>> score={}
>>> score["test1"]={}
>>> score["test2"]={}
>>> score[test1]["Pujara"]=211
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test1' is not defined
>>> score["test1"]["Pujara"]=211
>>> score["test1"]["Kohli"]=151
>>> score["test1"]["Rahane"]=123
>>> score["test2"]["Rahane"]=23
>>> score["test2"]["Kohli"]=183
>>> score["test2"]["Pujara"]=251
>>> score
{'test1': {'Pujara': 211, 'Kohli': 151, 'Rahane': 123}, 'test2': {'Rahane': 23, 'Kohli': 183, 'Pujara': 251}}
>>> d={}
>>> for l in "abcdefghi"
  File "<stdin>", line 1
    for l in "abcdefghi"
                       ^
SyntaxError: invalid syntax
>>> for l in "abcdefghi":
...   d[l] = l
... 
>>> d["1"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '1'
>>> d["d"]
'd'
>>> d["e"]
'e'
>>> d[""]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: ''
>>> d["l"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'l'
>>> 
shiraz@shiraz-Vostro-1550:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
shiraz@shiraz-Vostro-1550:~$ cd Documents
shiraz@shiraz-Vostro-1550:~/Documents$ cd Python
shiraz@shiraz-Vostro-1550:~/Documents/Python$ ls
binarySearch.py   __pycache__   selectionSort.py  speed4.py  speed8.py
insertionSort.py  quicksort.py  speed1.py         speed5.py
isort.py          randomize.py  speed2.py         speed6.py
mergesort.py      search.py     speed3.py         speed7.py
shiraz@shiraz-Vostro-1550:~/Documents/Python$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> score={}
>>> score[test1]["Pujara"]=211
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test1' is not defined
>>> test1={}
>>> score[test1]["Pujara"]=211
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> score[test1]={}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> 
