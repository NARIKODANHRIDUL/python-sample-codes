def pttrn():
    for r in range(1,6):
        for csp in range(1,(5-r)+1):
            print(" ",end='')
        for cst in range(1,2*r):
            print('*',end='')
        print()    
pttrn()

