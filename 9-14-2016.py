Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x = 10 + 2 * 5 + 3 / 2
>>> x
21.5
>>> x = "here" or "there"
>>> x
'here'
>>> x
'here'
>>> x
'here'
x
>>> 
>>> x
'here'
x
>>> 
>>> x
'here'
x
>>> 
>>> x
'here'
>>> x
'here'
>>> x
'here'
>>> x
'here'
x
>>> x = 2
>>> y = 8
>>> x **= y
>>> x
256
>>> x = 24 and 3600
>>> x
3600
>>> x
3600
>>> fahrenheit = float(90)
>>> celsius = (fahrenheit - 32.0) * 5.0 / 9.0
>>> x = celsius
>>> x
32.22222222222222
>>> a = True
>>> b = False
>>> x = a or b
>>> x
True
>>> x
True
>>> x
True
>>> x = "{2}{1}{0}".format(False, "s", 37)
>>> x
'37sFalse'
>>> a = "hello THERE     "
>>> x = a[0:5].upper()
>>> x+=" " + a[5:].lower().strip()
>>> x
'HELLO there'
>>> x = "{a}{c}{b}".format(a = 1, b = 2, c = 3)
>>> x
'132'
>>> x =  y[1] and y[3]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x =  y[1] and y[3]
TypeError: 'int' object is not subscriptable
>>> y = [True, False, True, True]
>>> x = y[1] and y[3]
>>> x
False
>>> x = len("snails * 3)
	
SyntaxError: EOL while scanning string literal
>>> x = len("snails" * 3)
>>> x
18
>>> x = "{:.3}".format(3.141567)
>>> x
'3.14'
>>> x = "Disney Land" or 1776 and 34
>>> x
'Disney Land'
>>> x = 7
>>> y = 3
>>> x = 7
>>> y = 2
>>> x = x//y
>>> x = x//y + 4
>>> x
5
>>> x = 7
>>> y = 2
>>> x = x//y + 4
>>> x
7
>>> x = 13
>>> x = y%2+5//2
>>> x
2
>>> 
