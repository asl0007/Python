# Python

NPTEL COURSE

Programming, Data Structures and Algorithms- https://nptel.ac.in/courses/106106145/
`````
ALGORITHM 
-it tells how to sytematically perform some task
-manipulate information
-compute numerical functions
-reorganize data
-optimization

PROGRAMMING language 
-describe steps
-determine sequence of steps

?> What makes a good program?
-correctness and efficiency
-readability
-ease of maintenance
-what you say and how you say it

PYTHON
-Interpreted language

Python2 = older version, static
Python3 = modern and current version

Compiler- It translates High Level language to Machine Level language

Interpreter- Itself a program that runs and directly uunderstandsto be executed
           -it executes statements from top to bottom        
          
Assignment statement - asssign a value to a name
           left hand side(name)
           right hand side(expression or value)
i=5 
j=2*i
j=j+5

type(e) returns the type of expression 'e'
-boolean values returns True and False
-there is no separate type char in python
-numeric 
1.Int   2.Float
-string(str)

int vs float
-Sequence is read off as a binary number
-division always produces a float
-float is a generalised form of int
-float number have mantissa and exponent
e.g  0.602 * 10^24
here 0.602 is mantissa and 24 is exponent

Comparison
'==' equals to
'!=' not equals to
'<' less than
'>' greater than
'<=' less than equal to
'>=' greater than equal to

type conversion
-str(78)= "78"
-int("123")=123
-int("1a2s")  yields an error

logical(and, or, not)

Text processing
-document preparation
-import / export spreadsheet data
-matching search queries to content

STRING
-enclosed in quotes
1.single('')
2.double("")
3.triple(''' ''')
-operation on string
--concatenation i.e addition of two string using '+' operator
--length of string i.e len(s)
-Extraction of string(slicing)
->A slice is a 'segment'of a string
-we cant update a string in place instead use slice and concatenation.

LISTS
-sequence of values
-types need not to be uniform
-extract value by position, slice
-for a string both single position and slice returns a string
-for a list, a single position returns a value while a slice returns a list
-nested list(list can contain other lists)
-lists are mutable i.e it can be updated in place
-A slice creates a new list from an old one
->omitting both end points gives a full slice
-concatenation always produces a new list
-adding an element to a list in place can be done using append() function
-append is a function that adds values/lists in the list 
-remove(x) function remove the first occurence of 'x' from the list
-reverse() it reverse the list in place
-sort() sort the list in ascending order
-index(x)find the leftmost position of 'x' in the list

values of type int, float, bool, str are immmutable


Control flow
-Need to vary computation steps as value change
-it determines order in which statements are executed
-conditional execution
-repeated execution(loops)
-function definitions
(A function is agroup of statements which performs a given task)
body is indented
return() statement exit and returns a value
passing a value to function-Argument value is substituted for a name
A function must be defined before it is invoked
-mutable values are affected while immutables are not during a function call
-recursive function (a function can call itself)
-functions are a good way to organize code in logical chunks

LINK LIST
-CREATE NODE
-INSERT NODE(BEG,END,SPECIFIC)
-DELETE NODE
-APPEND VALUE

-PRIORITY QUEUE(HEAP)

TREE
-INSERT
-DELETE
-TRAVERSAL

MEMOIZATION

DYNAMIC PROGRAMMING
-GRID PATHS
-LONGEST COMMON SUBWORD
-LONGEST COMMON SUBSEQUENCE
-MATRIX MULTIPLICATION
`````
