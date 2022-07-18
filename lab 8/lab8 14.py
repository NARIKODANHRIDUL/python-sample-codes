def fact(N):
    f=1
    for i in range(1,N+1):
        f=f*i
    return f
N=int(input('Enter a number :'))
print(fact(N),'is the factorial of',N)

