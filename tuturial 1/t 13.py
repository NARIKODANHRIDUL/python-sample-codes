l=int(input('enter the lower value of the range :'))
u=int(input('enter the upper value of the range :'))
for n in range(l,u):
    f=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            f=1
            break
    if f==0 and n!=1:
        print(n)

