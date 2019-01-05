def condition(x):
    if x==0:
        return(False)
    else:
        if x=="":
            return(False)
        else:
            if x==[]:
                return(False)
            else:
                return(True)
#>>> from condition import *
#>>> condition()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: condition() missing 1 required positional argument: 'x'
#>>> condition(9)
#True
#>>> condition("")
#False
#>>> condition('')
#False
#>>> condition([])
#False
#>>> condition(0)
#False

////Multiway branching////

def condition(x):
    if x==0:
        return(False)
    elif x=="":
        return(False)
    elif x==[]:
        return(False)
    else:
        return(True)
    
   #>>> from condition import *
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/home/mint/Desktop/condition.py", line 4
#    elif: x=="":
#        ^
#SyntaxError: invalid syntax
#>>> from condition import *
#>>> condition(0)
#False
#>>> condition([])
#False
#>>> condition('')
#False
#>>> condition("")
#False
#>>> condition(9)
#True
#>>> condition(gffgh)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'gffgh' is not defined
#>>> condition('gffgh')
#True
#>>> condition(687.8)
#True

