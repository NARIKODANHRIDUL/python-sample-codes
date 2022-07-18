x=int(input('Enter a number :'))
y=str(x)
s=0
for i in range(len(y)):
    a=x%10
    s=s+(a*a*a)
    x=x//10
if s==int(y):
    print(y,'is an Amstrong number')
else:
    print(y,'is not an Amstrong number')
