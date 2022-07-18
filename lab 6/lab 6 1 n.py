for r in range(1,10):
     if r<=5:
        for s1 in range (5-r,0,-1):
            print(' ',end='')
        for c1 in range (1,r+1):
            print("*",end='')
        print()
    
     else:
        for s2 in range (r-5,0,-1):
            print(' ',end='')
        for c2 in range(10-r,0,-1):
            print('*',end='')
        print()   
