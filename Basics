Play with python in the interpreter


>>> from math import *
>>> sqrt(25)
5.0
>>> log(1)
0.0
>>> sin(45)
0.8509035245341184
>>> tan(45)
1.6197751905438615
>>> tan(pi/4)
0.9999999999999999
>>> pi
3.141592653589793
>>> 98//45        
2
>>> 8/2.5
3.2
>>> 7*9
63
>>> 9%5
4
>>> i=5
>>> type(i)
<class 'int'>
>>> j=9.99
>>> j
9.99
>>> type(j)
<class 'float'>
>>> i=j*4
>>> i
39.96
>>> type(i)
<class 'float'>
>>> 9//2
4
>>> 2**3
8

#BOOL 
//A sample program 

def divides(m,n):
    if (n%m==0):
        return(True)
    else:   
        return(False)
def even(n):
    return(divides(2,n))
def odd(n):
    return(not divides(2,n))

//output

>>> from div import *
>>> odd(5)
True
>>> odd(34)
False
>>> even(5)
False
>>> even(34)
True
>>> divides(8,3)
False
>>> divides(4,2)
False
>>> divides(2,4)
True


////Strings

>>> string="String"
>>> string
'String'
>>> type(string)
<class 'str'>
>>> char='x'
>>> type(char)
<class 'str'>
>>> char
'x'
>>> x="Hi! who is there with you?"        
>>> x
'Hi! who is there with you?'
>>> y="Hey 'there"
>>> y
"Hey 'there"
>>> y='HI "there"'       
>>> y
'HI "there"'
>>> z='''Newbie,"New Love",'Alter'.'''
>>> z
'Newbie,"New Love",\'Alter\'.'
>>> x='''first
... second
... third'''
>>> x
'first\nsecond\nthird'
>>> x[3]
's'
>>> x[1:5]
'irst'
>>> x[:9]
'first\nsec'
>>> x[9:]
'ond\nthird'
>>> x[:]
'first\nsecond\nthird'
>>> x[-7]
'd'
>>> x[-6]
'\n'
>>> x+y
'first\nsecond\nthirdHI "there"'
>>> x+y+z
'first\nsecond\nthirdHI "there"Newbie,"New Love",\'Alter\'.'
>>> len(x)
18
>>> x[-2:3]
''
>>> x[-2:-5]     
''
>>> x[:90]
'first\nsecond\nthird'
>>> x[:15]+"asdf"           
'first\nsecond\nthasdf'


////////////LISTS/////////

>>> factors=[1,2,3,4,6,12]
>>> factors
[1, 2, 3, 4, 6, 12]
>>> names=['Amit','Deepak','Pankaj','Shiraz Ali']
>>> names
['Amit', 'Deepak', 'Pankaj', 'Shiraz Ali']
>>> names[-3:]
['Deepak', 'Pankaj', 'Shiraz Ali']
>>> names[3][-3:]
'Ali'
>>> mixed=[1,True,"Love"]
>>> mixed
[1, True, 'Love']
>>> mixed[1:]
[True, 'Love']
>>> factors[-5]
2
>>> factors[4]
6
>>> len(factors)
6
>>> len(names)
4
>>> len(mixed)
3

>>> nested=[[1,[2,3,[4,5]],6],7,["Program"]]
>>> nested
[[1, [2, 3, [4, 5]], 6], 7, ['Program']]
>>> nested[1]
7
>>> nested[2]
['Program']
>>> nested[2][0][-3:]
'ram'
>>> nested[1]=nested[2]
>>> nested
[[1, [2, 3, [4, 5]], 6], ['Program'], ['Program']]
>>> nested[2]=nested[1]
>>> nested
[[1, [2, 3, [4, 5]], 6], ['Program'], ['Program']]
>>> nested[2]=99    
>>> nested
[[1, [2, 3, [4, 5]], 6], ['Program'], 99]
>>> nested[0][1][2][0]
4
>>> nested[0][1][2]=nested[2]
>>> nested
[[1, [2, 3, 99], 6], ['Program'], 99]
>>> nested[0][1]=nested[1]
>>> nested
[[1, ['Program'], 6], ['Program'], 99]
>>> nested[1]=factors
>>> nested
[[1, ['Program'], 6], [1, 2, 3, 4, 6, 12], 99]
>>> nested[2]=names
>>> nested
[[1, ['Program'], 6], [1, 2, 3, 4, 6, 12], ['Amit', 'Deepak', 'Pankaj', 'Shiraz Ali']]

IMMUTABLE-(int,float,bool) values
>>> x=5
>>> y=x
>>> y
5
>>> x
5
>>> x=7
>>> y
5
>>> x
7
>>> f=2.5
>>> d=9.90
>>> f
2.5
>>> d
9.9
>>> g=f
>>> g
2.5
>>> f=7.7
>>> f
7.7
>>> g
2.5

LISTS ARE MUTABLES
>>> list1=[1,2,3,4]
>>> list2=[1,2,3,4]
>>> list3=list2
>>> list1
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> list3
[1, 2, 3, 4]
>>> list2[2]=6
>>> list1
[1, 2, 3, 4]
>>> list2 
[1, 2, 6, 4]
>>> list3
[1, 2, 6, 4]
>>> list2=list1[:]
>>> list2[1]=9
>>> list2
[1, 9, 3, 4]
>>> list1
[1, 2, 3, 4]
>>> list1==list2
False
>>> list2==list3
False
>>> list3
[1, 2, 6, 4]
>>> list3[2]=3
>>> list3
[1, 2, 3, 4]
>>> list3=list1+list2
>>> list3
[1, 2, 3, 4, 1, 9, 3, 4]
>>> list2=list3
>>> list2
[1, 2, 3, 4, 1, 9, 3, 4]
>>> list1
[1, 2, 3, 4]
>>> list1 is list2
False
>>> list1 is list3
False
>>> list2 is list3
True
>>> list3 is list2
True
>>> list2==list3
True


////type conversion///
str(78)="78"
int("3231")=3231
int("54g") will yield an  error.


////Extending a list////

>>> list1=list(range(0,5))
>>> list1
[0, 1, 2, 3, 4]
>>> list2=list(range(5,10))
>>> list2
[5, 6, 7, 8, 9]
>>> list3=list2
>>> list3.append(10)
>>> list3
[5, 6, 7, 8, 9, 10]
>>> list2
[5, 6, 7, 8, 9, 10]
>>> list3.remove(10)
>>> list2
[5, 6, 7, 8, 9]
>>> list3
[5, 6, 7, 8, 9]
>>> list1.extend(list2)
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list1[8:]=[10]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 10]
>>> list1[2:7]=[4]
>>> list1
[0, 1, 4, 7, 10]
>>> list1[1]=[1,2,3,4]
>>> list1
[0, [1, 2, 3, 4], 4, 7, 10]
>>> 
