n=int(input('Enter a number :'))
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
    else:
        s=s-i
print(s,'is the calculated value for thre givrn function')
