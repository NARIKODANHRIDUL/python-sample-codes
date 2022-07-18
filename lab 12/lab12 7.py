r=[]
q=[]
a=[]
n=int(input('enter number of records: '))
for i in range(n):
    s=[]
    print('\n',i+1,'th students details:-',sep='')
    nm=input('name :')
    gr=float(input('grade :'))
    s.append(nm)
    s.append(gr)
    q.append(gr)
    r.append(s)
q=list(set(q))
q.sort()
m=q[1]
for i in range(len(r)):
    if r[i][1]==m:
        a.append(r[i][0])
a.sort()
for i in a:
    print(i)


    
    
