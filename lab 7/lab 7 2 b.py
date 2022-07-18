n=int(input('Enter the number of test cases :'))
l=[]
for a in range(n):
    w=int(input())
    l.append(w)
for x in range(n):
    f=0
    for a3 in range(l[x]//3):
        for a5 in range(l[x]//5):
            if f==1:
                break
            for a7 in range(l[x]//7):
                if a3*3+a5*5+a7*7==l[x]:
                    print(a3,a5,a7)
                    f=1
    if f==0:
        print(-1)
