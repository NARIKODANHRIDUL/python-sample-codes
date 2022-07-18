def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input('Enter a number: '))
print(fibo(n),' is the ',n,'th number of fibonacci series',sep='')

