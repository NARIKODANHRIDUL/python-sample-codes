n=int(input('enter a number :'))
print('factor are : ')
for i in range(1,(int(n/2)+1)):
    if n%i==0:
        print(i,end=' ')
print(n)
        
        
        
