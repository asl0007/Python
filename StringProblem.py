Task
Store the below string in a variable.
‘the quick brown fox jumps Over the lazy Dog’
    1) Find the number of words in the sentence
    2) Print all words having count of characters an odd number
    3) Number of words starting with an Upper-case character
    4) Count the total number of vowels in the sentence
    5) Form a sentence by printing all the words in the reverse order.
    6) Remove all the spaces from the string
    7) Make all the first character of each word upper case
    8) Take a random word from the sentence, count the occurrences. (Ignore the upper-case and lower-case)
    9) Print the first word and the last word of the string
    
Example:
Output
#1 : 9
#2 : the quick brown fox jumps the dog
#3 : 2
#4 : 11
#5 : Dog lazy the Over jumps fox brown quick the
#6 : thequickbrownfoxjumpsOverthelazyDog
#7 : The Quick Brown Fox Jumps Over The Lazy Dog
#8 : Random word: the
Count: 2
#9 : the dog

Solution 
#Store the below string in a variable.
#‘the quick brown fox jumps Over the lazy Dog’
>>>var = "the quick brown fox jumps Over the lazy Dog"
#1) Find the number of words in the sentence
>>> var = "the quick brown fox jumps Over the lazy Dog"
>>> words = str.split(var)
>>> print(len(words))
9
#2) Print all words having count of characters an odd number
>>> for word in words:
...   if(len(word)%2 != 0):
...     print (word)
... 
the
quick
brown
fox
jumps
the
Dog
#3) Number of words starting with an Upper-case character
>>> for word in words:
...   if word[0].isupper():
...     print (word)
... 
Over
Dog
#4)Count the total number of vowels in the sentence
>>> count = 0
>>> vowel = set("aeiouAEIOU")
>>> for alphabet in var:
...   if alphabet in vowel:
...     count = count + 1
... 
>>> print(count)
11
#5) Form a sentence by printing all the words in the reverse order.
>>> rev_words = list(reversed(words))
>>> print(" ".join(rev_words))
Dog lazy the Over jumps fox brown quick the
#6) Remove all the spaces from the string
>>> print(var.replace(" ", ""))
thequickbrownfoxjumpsOverthelazyDog
#7) Make all the first character of each word upper case
>>> for word in words:
...   print(str.capitalize(word))
... 
The
Quick
Brown
Fox
Jumps
Over
The
Lazy
Dog
#8)Take a random word from the sentence, count the occurrences. (Ignore the upper-case and lower-case)
>>> counts = dict()
>>> for word in words:
...         if word in counts:
...             counts[word] += 1
...         else:
...             counts[word] = 1
…
>>> print(counts['the'])
2
#9)Print the first word and the last word of the string
>>> first, *middle, last = var.split()
>>> print(first, last)
the Dog
