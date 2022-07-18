x=int(input('Enter the number of copies :'))
y=int(input('Enter the number of orginal :'))
f=0
for i in range(-1,x+y+1):
    if x==(y+1+2*i):
        print('YES')
        f=1
        break
if f==0:
    print('NO')

