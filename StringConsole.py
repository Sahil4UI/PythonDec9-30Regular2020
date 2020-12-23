Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String
>>> x = "hello"
>>> type
<class 'type'>
>>> type(x)
<class 'str'>
>>> x = 'hello'
>>> type(x)
<class 'str'>
>>> # single/double quotes are used to denote a single line or single para string
>>> x = 'Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020.[29] Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows).'
SyntaxError: invalid syntax
>>> x = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020.[29] Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows)."
SyntaxError: EOL while scanning string literal
>>> x = '''Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020.[29] Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows).'''
>>> print(x)
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020.[29] Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows).
>>> # ''' is used for multi line string
>>> #'Python' is a programming language
>>> x = ''Python' is a programming language'
SyntaxError: invalid syntax
>>> x = " 'Python' is a programming language'
SyntaxError: EOL while scanning string literal
>>> x = " 'Python' is a programming language"
>>> x
" 'Python' is a programming language"
>>> print(x)
 'Python' is a programming language
>>> x = ' "Python" is a programming language'
>>> x = " \"Python\" is a programming language"
>>> # -> \ -> escape sequence / character
>>> print(x)
 "Python" is a programming language
>>> x =' "Python" is a \n programming language'# \n-next line
>>> print(x)
 "Python" is a 
 programming language
>>> x = ' "Python" is a\tprogramming language'#tab-4times of space
>>> print(x)
 "Python" is a	programming language
>>> #slicing
>>> #indexing
>>> x
' "Python" is a\tprogramming language'
>>> x[0]
' '
>>> x[1]
'"'
>>> print(x[1])
"
>>> print(x[0])
 
>>> print(x[2])
P
>>> x = "python"
>>> x[0]
'p'
>>> x[1]
'y'
>>> x[2]
't'
>>> x[3]
'h'
>>> x[4]
'o'
>>> x[5]
'n'
>>> x = "welcome to our python programming class"
>>> x
'welcome to our python programming class'
>>> x[-1]
's'
>>> x[-2]
's'
>>> x[-5]
'c'
>>> #slicing
>>> #string ->Substring
>>> x
'welcome to our python programming class'
>>> #x[string index:ending index]
>>> x[0:6]
'welcom'
>>> #ending index->n-1 -> +1
>>> x[0:7]
'welcome'
>>> #x[starting index:ending index:inc/dec]
>>> x
'welcome to our python programming class'
>>> x[0:7:1]
'welcome'
>>> x[0:7:2]
'wloe'
>>> x
'welcome to our python programming class'
>>> x[10:]
' our python programming class'
>>> x[:10]
'welcome to'
>>> x[:]
'welcome to our python programming class'
>>> x
'welcome to our python programming class'
>>> #find the reverse of string
>>> x[-1:]
's'
>>> x[-1:-10:1]
''
>>> x[-1:-10:-1]
'ssalc gni'
>>> x[-1::-1]
'ssalc gnimmargorp nohtyp ruo ot emoclew'
>>> #String methods(inbuilt functions)
>>> x
'welcome to our python programming class'
>>> x.upper()
'WELCOME TO OUR PYTHON PROGRAMMING CLASS'
>>> x
'welcome to our python programming class'
>>> #String - immutable
>>> x = x.upper()
>>> x
'WELCOME TO OUR PYTHON PROGRAMMING CLASS'
>>> x.lower()
'welcome to our python programming class'
>>> x.casefold()
'welcome to our python programming class'
>>> x
'WELCOME TO OUR PYTHON PROGRAMMING CLASS'
>>> x.capitalize()
'Welcome to our python programming class'
>>> x.title()
'Welcome To Our Python Programming Class'
>>> x
'WELCOME TO OUR PYTHON PROGRAMMING CLASS'
>>> x = x.title()
>>> x
'Welcome To Our Python Programming Class'
>>> x.swapcase()
'wELCOME tO oUR pYTHON pROGRAMMING cLASS'
>>> x
'Welcome To Our Python Programming Class'
>>> x.replace("Python","C++")
'Welcome To Our C++ Programming Class'
>>> x
'Welcome To Our Python Programming Class'
>>> x.isalpha()
False
>>> x = "welcomeHome"
>>> x.isalpha()
True
>>> x = "hi123"
>>> x.isalpha()
False
>>> x.isalnum()
True
>>> x = "3453534"
>>> x.isdigit()
True
>>> x = 'Welcome To Our Python Programming Class'
>>> x.count('e')
2
>>> x.count('o)
	
SyntaxError: EOL while scanning string literal
>>> x.count('o')
4
>>> x
'Welcome To Our Python Programming Class'
>>> x.index('W')
0
>>> x.index(e)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    x.index(e)
NameError: name 'e' is not defined
>>> x.index('e')
1
>>> x
'Welcome To Our Python Programming Class'
>>> x('e',0)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    x('e',0)
TypeError: 'str' object is not callable
>>> x.index('e',0)
1
>>> x
'Welcome To Our Python Programming Class'
>>> x.index('e',2)
6
\
>>> x.index('z')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    x.index('z')
ValueError: substring not found
>>> x.find('e')
1
>>> x.find('e',2)
6
>>> x.find('z')
-1
>>> #-1 value not found
>>> x
'Welcome To Our Python Programming Class'
>>> x.rfind('o')
24
>>> 
