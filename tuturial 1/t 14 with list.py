l=[]
a=list(map(int,input().split()))
l.append(a)
s=0
for x in range(l[0][2]):
    s=s+(x+1)
c=s*l[0][0]
b=c-l[0][1]
if b>0:
    print('he has to borrow $',b,'from his friend')
else:
    print('no need to borow')
