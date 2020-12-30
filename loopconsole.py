Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

0
1
2
3
4
>>> for i in range(1,5):
	print(i)

1
2
3
4
>>> for i in range(4,0,-1):
	print(i)

4
3
2
1
>>> for i in reversed(range(1,5)):
	print(i)

4
3
2
1
>>> """
"""
'\n'
>>> """
2X1=2
2X2=4
.
.
2X10=20"""
'\n2X1=2\n2X2=4\n.\n.\n2X10=20'
>>> x = 1
>>> print("2 X ",x,'=',2*x)
2 X  1 = 2
>>> print("2 X {} = {}".format(x,2*x))
2 X 1 = 2
>>> print(f"2 X {x} = {2*x}")
2 X 1 = 2
>>> for i in range(1,11):
	print(f"2 X {i} = {2*i}")

2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
>>> 
