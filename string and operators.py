Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String methods
>>> x = "python'
SyntaxError: EOL while scanning string literal
>>> x = 'python'
>>> x
'python'
>>> len(x)
6
>>> x = "Java"
>>> len(x)
4
>>> x
'Java'
>>> x.center(2)
'Java'
>>> x.center(4)
'Java'
>>> x.center(5)
' Java'
>>> x.center(6)
' Java '
>>> x.center(20)
'        Java        '
>>> x.center(21)
'         Java        '
>>> x.center(21,'*')
'*********Java********'
>>> x.center(21,'-')
'---------Java--------'
>>> x = x.center(22)
>>> x
'         Java         '
>>> x.lstrip()
'Java         '
>>> x.rstrip()
'         Java'
>>> x.strip()
'Java'
>>> x='---------Java--------'
>>> x.strip()
'---------Java--------'
>>> x.strip('-')
'Java'
>>> x="this is our python programming class"
>>> x.split()
['this', 'is', 'our', 'python', 'programming', 'class']
>>> x.split()[0]
'this'
>>> x.split()[-1]
'class'
>>> x = "hi"
>>> x.zfill(1)
'hi'
>>> x.zfill(2)
'hi'
>>> x.zfill(3)
'0hi'
>>> x.zfill(5)
'000hi'
>>> #zfill->zerofill
>>> x='000hi'
>>> x[0]
'0'
>>> x.zfill(0)
'000hi'
>>> x="hi"
>>> x.zfill(0)
'hi'
>>> x.zfill(-10)
'hi'
>>> #AScii (American Standard Code for Information Interchange) code
>>> #ord , chr
>>> ord('A')
65
>>> #ord- ORdinal function-it will return the ascii value of the character
>>> #chr-on behalf of ascii value, it will return the character
>>> chr(69)
'E'
>>> chr(65)
'A'
>>> chr(125)
'}'
>>> chr(200)
'È'
>>> chr(210)
'Ò'
>>> chr(250)
'ú'
>>> chr(500)
'Ǵ'
>>> #Operators
>>> #Arithmetic operator -> +,-,/,*,//,**
>>> #relational Operator-(>,<,>=,<=,!=,==)
>>> 4!=3#not equals
True
>>> 4==4#equality operator
True
>>> #relational -> conditional Operator
>>> #logical operator->and , or , not
>>> #and-for true, all conditions must be true
>>> 1>5 and 5==5 and 4==4
False
>>> 1==1 and 5==5
True
>>> #or ->for true , atleast one condition must be true
>>> 5!=5 or 5==5
True
>>> #== equality operator
>>> #= assignment operator
>>> 4 =4
SyntaxError: cannot assign to literal
>>> 4==4
True
>>> x = 5
>>> #not-> True-False,False-True
>>> 5==5
True
>>> not 5==5
False
>>> 
>>> #Membership operator
>>> vowles='aeiou'
>>> vowels = 'aeiou'
>>> vow
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    vow
NameError: name 'vow' is not defined
>>> vowels
'aeiou'
>>> 'x' in vowels
False
>>> 'a' in vowels
True
>>> 'x' not in vowels
True
>>> #Identity Operator
>>> x=4
>>> y=4
>>> x is y
True
>>> x is not y
False
>>> 
