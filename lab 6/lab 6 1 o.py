for r in range(1,10):
     if r<=5:
         for s1 in range(5-r):
             print(' ',end='')
         for c1 in range(((r-1)*2)+1):
             print('*',end='')
         print()    
     else:
         for s2 in range(r-5):
             print(' ',end='')
         for c2 in range(((9-r)*2)+1):
             print('*',end='')
         print()    
