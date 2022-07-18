def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
n=int(input('enter a number:'))
print(fibo(n))
