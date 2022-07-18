n=int(input('Enter a number :'))
s=0
for i in range(1,(n//2)+1):
    if n%i==0:
        s=s+i
if s>n:
    print(n,'is an Abundant Number')
else:
    print(n,'is not an Abundant Number')
