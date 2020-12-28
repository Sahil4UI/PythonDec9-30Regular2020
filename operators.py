Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bitwise operator
>>> # bitwise and operator- &
>>> 5 & 19
1
>>> 53 & 98
32
>>> #bitwise or operator - |
>>> 53 | 98
119
>>> #btwise- left shift & right shift operators
>>> 12<<1#left shift operators
24
>>> 12<<2
48
>>> 56>>1
28
>>> 5>>1
2
>>> #bitwise not operator
>>> ~ 20
-21
>>> 
>>> # ~ -> complement
>>> ~ -20
19
>>> #Assignment Operator
>>> x = 34
>>> 5=5
SyntaxError: cannot assign to literal
>>> 5==5
True
>>> x
34
>>> x += 1#x=x+1
>>> x
35
>>> x -= 12
>>> x
23
>>> x *= 2
>>> x
46
>>> x /= 2
>>> x
23.0
>>> 23 ** 0.5
4.795831523312719
>>> x **= 0.5
>>> x
4.795831523312719
>>> x %= 12
>>> x
4.795831523312719
>>> x //= 2
>>> x
2.0
>>> x & = 5
SyntaxError: invalid syntax
>>> x&=5
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x&=5
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
>>> x = 5
>>> x &= 2
>>> x
0
>>> #Membership operator
>>> vowels = "aeiou"
>>> 'a' in vowels
True
>>> #identity operator
>>> x = 5
>>> y = 5
>>> x is y
True
>>> #list
>>> x = [1,2,3,4,5]
>>> y = [1,2,3,4,5]
>>> x is y
False
>>> id(x)
2649034636672
>>> id(y)
2649034697024
>>> x = 5
>>> y = 10
>>> y=5
>>> x
5
>>> y
5
>>> id(x)
2648993720752
>>> id(y)
2648993720752
>>> x = [1,2,3,4,5]
>>> y = x
>>> 
>>> id(x)
2649003447488
>>> id(y)
2649003447488
>>> x
[1, 2, 3, 4, 5]
>>> y
[1, 2, 3, 4, 5]
>>> x.pop()
5
>>> x
[1, 2, 3, 4]
>>> y
[1, 2, 3, 4]
>>> x is y
True
>>> 
