#add first 10 natural numbers
'''
result = 0
for i in range(1,11):
    result += i #result = result +i
'''

'''
import math
result = 0
for i in range(1,11):
    result += (2*i-1)/math.factorial(2*i)

print(result) 
'''
'''
x = int(input("Enter Number"))
temp =x
res = 0
digits = len(str(x))
print("no of digits =",digits)
for i in range(digits):
    rem = x%10`
    res = res*10+rem
    x = x//10

if res == temp:
    print("pallindrome")
else:
    print("not pallindrome")'''
'''
x = int(input("Enter Number"))
temp =x
res = 0
digits = len(str(x))
print("no of digits =",digits)
for i in range(digits):
    rem = x%10`
    res = res+rem**3
    x = x//10

if res == temp:
    print("Armstrong")
else:
    print("not an Armstrong No")
'''
x = int(input("Enter Number"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("prime")
        
