# **_**
# *___* 
# _____ 
# *___* 
# **_**

n = 2
for i in range(n):
    for j in range(n-i,0,-1):
        print('*',end='')
    for _ in range(i+1):
        print('  ',end='')
    for j in range(n-i,0,-1):
        print('*',end='')
    print()
for i in range(n+1):
    for j in range(i):
        print('*',end='')
    for _ in range(n-i,-1,-1):
        print('  ',end='')
    for j in range(i):
        print('*',end='')
    print()

print()

# __*__
# _***_
# *****
# _***_
# __*__

n = 3
for i in range(1,n+1):
    for k in range(n-i):
        print(' ',end='')
    for j in  range(2*i - 1):
        print('*',end='')
    print()
for i in range(1,n):    
    for k in range(i):
        print(' ',end='')
    for j in range(2*((n-1)-i)+1):
        print('*',end='')
    print()
    
print()       

# *
# **
# *_* 
# *__*
# *****

for i in range(0,5):
    for j in range(0,i+1):
        if i==0 or j==0 or j== i or i == 4:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()

# ***** 
# *___*
# *___*
# *___*
# *****

for i in range(0,5):
    for j in range(0,5):
        if i == 0 or j == 0 or i == 4 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print()   

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

count = 1
for i in range(0,5):
    for j in range(0,i+1):
         print(count,end=" ")
         count += 1
    print()  