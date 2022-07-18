def fibo(n):
    x,y=0,1
    print(x)
    print(y)
    for i in range(n-2):
        t=x
        x=y
        y=t+y
        print(y)        
n=int(input('Enter a number :'))
fibo(n)

