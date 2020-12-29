#CONDITIONAL STATEMENTS - Decision making-if-else
#1 condition -  if statement
#2 condition - if-else
#more than 2 conditions - if -elif
'''
x = int((input("Enter a Number")))
if x%2==0:
    print("Even Number")
else:
    print("odd")
'''
'''
x = int((input("Enter Number 1:")))
y = int((input("Enter Number 2:")))
z = int((input("Enter Number 3:")))


if x>y>z:
    print(x," is largest")
elif x==y==z:
    print("all are equal")
elif y>z:
    print(y," is largest")
else:
    print(z," is largest")
'''
'''
if x>y and x>z:
    print(x," is largest")
elif x==y==z:
    print("all are equal")
elif y>z:
    print(y," is largest")
else:
    print(z," is largest")
'''

x = int((input("Enter Side 1:")))
y = int((input("Enter Side 2:")))
z = int((input("Enter Side 3:")))

if x+y>z and y+z>x and z+x>y:
    if x==y or y==z or x==z:
        print("Isoceles Traingle")
    elif x**2 == y**2+z**2 or y**2 == x**2+z**2 or z**2 == x**2+y**2:
        print("Right angle Traingle")
    elif x==y==z:
        print("Equilateral Traingle")
    else:
        print("scalene traingle")
else:
    print("Traingle is Imaginary")


#
