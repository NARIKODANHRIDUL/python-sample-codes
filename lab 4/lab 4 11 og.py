a=int(input('enter a value for A: '))
b=int(input('enter a value for B: '))
k=int(input('enter a value for K: '))
p=((k//2)*a)-((k//2)*b)
q=(((k//2)+1)*a)-((k//2)*b)
print('The position of the cat at the end is ',end='')
if k//2==0:
    print(p,end=' ')
else:
    print(q,end=' ')
print('units away from the origin')
