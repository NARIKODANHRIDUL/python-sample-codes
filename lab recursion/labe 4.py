def sod(n):
    if (n//10==0):
        return n
    else:
        return n%10+sod(n//10)
n=int(input('Enter a number:'))
print('sum of the digits =',sod(n))

