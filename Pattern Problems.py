'''
for i in range(1,4):
    for j in range(0,i):
        print(i,j)
'''

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(i):
        print('*',end='')
    print()
'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''    
'''
    *
   ***
  *****
 *******
*********
'''
'''
for i in range(1,6):
    print(' '*(5-i)+'*'*(2*i-1))
'''
