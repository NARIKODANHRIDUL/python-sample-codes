def prfct(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s=s+i
    if s==n:
        print('Given number is a perfect number')
    else:
        print('Given number is NOT a perfect number')
n=int(input('enter a number :'))
prfct(n)

