print('*')
for r in range(1,10):
    print('*',end='')
    if r<=5:
        for c1 in range(1,r+1):
            print(c1,end='')
        for c2 in range(r-1,0,-1):
            print(c2,end='')  
    else:
        for c3 in range(1,11-r):
            print(c3,end='')
        for c4 in range(9-r,0,-1):
            print(c4,end='')    
    print('*',end='')
    print()
print('*')
