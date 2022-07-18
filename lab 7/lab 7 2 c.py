n=int(input('Enter the number of test cases:'))
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
for x in range(n):
    if (l[x][0]%2==0 and l[x][1]%2==0) or (l[x][0]%2==1 and l[x][1]%2==1):
        if (l[x][0])>=(l[x][1]):
            print(2*(l[x][0]))
        else:
            print(2*(l[x][1]))
    else:
        print((l[x][0])+(l[x][1]))
        
