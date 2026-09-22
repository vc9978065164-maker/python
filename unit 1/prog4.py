Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>"""Write a program to demonstrate string 
operations including slicing formatting and 
built-in string functions"""

str = "vivek chauhan"
>>> 
>>> print(str.upper())
VIVEK CHAUHAN
>>> print(str.lower())
vivek chauhan
>>> print(str.capitalize())
Vivek chauhan
>>> print(str.split(" "))
['vivek', 'chauhan']
>>> print(str.count())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(str.count())
TypeError: count expected at least 1 argument, got 0
>>> print(len(str))
17
>>> print(str.replace("v","V"))
Vivek chauhan
