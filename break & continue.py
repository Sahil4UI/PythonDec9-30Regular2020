Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #break
>>> for i in range(1,1000000):
	print(i)
	if i==10:
		break

1
2
3
4
5
6
7
8
9
10
>>> #continue
>>> for i in range(1,11):
	if i%2==0:
		continue
	print(i)

1
3
5
7
9
>>> 