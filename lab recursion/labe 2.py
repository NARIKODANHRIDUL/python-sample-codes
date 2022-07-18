def sem(n):
    if n==1:
        return 1
    else :
        return n+sem(n-1)
n=int(input('Enter a number :'))
print(sem(n),'is the sum of',n,'natural numbers')

