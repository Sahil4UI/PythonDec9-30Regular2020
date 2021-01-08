'''
1
01
010
1010
10101
'''
'''
x=1
for i in range(1,6):
    for j in range(i):
        if x%2==0:
            print(0,end='')
        else:
            print(1,end='')
        x+=1
    print()
'''
'''
1
10
101
1010
10101
'''
'''
for i in range(1,6):
    for j in range(i):
        if (j+1)%2==0:
            print(0,end='')
        else:
            print(1,end='')
    print()
'''
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
