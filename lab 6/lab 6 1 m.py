for r in range (1,10):
    if r<=5:
        for c1 in range (1,r+1):
            print("*",end='')
        print()
    else:
        for c2 in range(10-r,0,-1):
            print('*',end='')
        print()   
