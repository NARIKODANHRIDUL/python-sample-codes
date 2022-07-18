l=[]
n=int(input('enter the number of elements :'))
for i in range(n):
    print('Enter the ',i+1,'th number :',sep='',end='')
    a=input()
    l.append(a)
l=l[::-1]
print('reversed list is :- \n',l)

