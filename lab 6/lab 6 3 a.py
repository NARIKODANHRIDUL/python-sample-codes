n=int(input('Enter a value for n :'))
x=0
for i in range(1,n+1):
    y=0
    for j in range(1,i+1):
        y=y+j
    x=x+y
print('sum of the given sequence is',x)     
