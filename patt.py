'''
*    *
*    *
******
*    *
*    *

'''
'''
for i in range(1,6):
    for j in range(1,7):
        if (i==3) or (j==1 or j==6):
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    print(" "*(5-i),end='')
    for j in range(i):
        print("* ",end='')
    print()
        
