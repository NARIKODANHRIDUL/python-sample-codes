n=int(input('Enter the number of programming qns:'))
l=[]
d=0
for i in range(n):
    a= list(map(int,input().split())) 
    l.append(a)
for x in range(n):
    c=0
    for y in range(3):
        if l[x][y]==1:
            c+=1
    if c>=2:
        d+=1
print(d)        
        
        
