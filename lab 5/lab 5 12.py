n=int(input('enter a number :'))
l=len(str(n))
s=0
for i in range(l):
    r=n%10
    s=s+r
    n=n//10
print("sum of the digit =",s)
    
