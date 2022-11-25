Python 3.7.5 (default, Dec  9 2021, 17:04:37) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> quantity= 3
>>> itemno=10
>>> price=50.50
>>> myorder="i want{}pieces of item{}for{}dollars."
>>> print(myorder.format(itemno,quantity,price))
i want10pieces of item3for50.5dollars.
>>> this ={"apple","orange","banana"}
>>> print("banana" in this)
True
>>> a=input("enter two numbers")
enter two numbers
>>>  a=("enter two numbers")
 
SyntaxError: unexpected indent
>>> 
========================================================== RESTART: /home/mca/Desktop/devadath/sum of 2nos.py ==========================================================
enter num1:5
enter num2:41
sum is: 46
>>> 
========================================================= RESTART: /home/mca/Desktop/devadath/greatest amng2.py ========================================================
enter num1:17
enter num2:-22
17 is greater
>>> 
========================================================= RESTART: /home/mca/Desktop/devadath/greatest amng3.py ========================================================
enter num1:5
enter num2:1
enter num3:8
8 is greater
>>> for i in range(0,10,2):
	print(i,end="")
	print()

	
0
2
4
6
8
>>> 
>>> for x in range(6)
SyntaxError: invalid syntax
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> if x==3;
SyntaxError: invalid syntax
>>> break;
SyntaxError: 'break' outside loop
>>> 
============================================================= RESTART: /home/mca/Desktop/devadath/break.py =============================================================
0
finally finished
1
finally finished
2
finally finished
3
>>> 
======================================================== RESTART: /home/mca/Desktop/devadath/leap year or not.py =======================================================
enter a year2002
Traceback (most recent call last):
  File "/home/mca/Desktop/devadath/leap year or not.py", line 2, in <module>
    if(a%400 ==0)or (a%4 ==0 and a%100!=0):
TypeError: not all arguments converted during string formatting
>>> 
============= RESTART: /home/mca/Desktop/devadath/leap year or not.py ============
enter a year 2000
Traceback (most recent call last):
  File "/home/mca/Desktop/devadath/leap year or not.py", line 2, in <module>
    if(a%400 ==0)or (a%4 ==0 and a%100!=0):
TypeError: not all arguments converted during string formatting
>>> 
============= RESTART: /home/mca/Desktop/devadath/leap year or not.py ============
enter a year2000
Traceback (most recent call last):
  File "/home/mca/Desktop/devadath/leap year or not.py", line 2, in <module>
    if(a%400==0)or (a%4==0 and a%100!=0):
TypeError: not all arguments converted during string formatting
>>> 
============= RESTART: /home/mca/Desktop/devadath/leap year or not.py ============
enter a year2000
leap year
>>> 
============= RESTART: /home/mca/Desktop/devadath/leap year or not.py ============
enter a year2010
not a leap year
>>> 
