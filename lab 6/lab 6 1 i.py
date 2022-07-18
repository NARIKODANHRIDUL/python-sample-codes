for r in range(1,6):
    for c in range(1,r+1):
        print(c,end='')
    for c1 in range(((5-r)*2)):
        print(' ',end='')
    for c2 in range(r,0,-1):
        print(c2,end='')
    print()
    
