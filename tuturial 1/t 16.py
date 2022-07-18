a=int(input('Enter value of a :'))
b=int(input('Enter value of b :'))
s,n5,n2,n1=0,0,0,0
while(a%b!=0):
    if a%b>=5:
        a=a+(b-5)
        s+=1
        n5+=1
    elif a%b>=2:
        a=a+(b-2)
        s+=1
        n2+=1
    elif a%b==1:
        a=a+(b-1)
        s+=1
        n1+=1
print(s,'steps are required')
print('\n5 is added',n5,'times')
print('2 is added',n2,'times')
print('1 is added',n1,'times')
        
        
