l=[]
n=int(input('enter the number of elements :'))
for i in range(n):
    print('Enter the ',i+1,'th number :',sep='',end='')
    na=input()
    l.append(na)
l.pop()
l.pop(0)
print(l)

