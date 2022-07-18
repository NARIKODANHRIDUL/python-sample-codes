rec=[]
mark=[]
n=int(input('Enter the number of students :'))
for i in range(n):
    std=[]
    print('enter',i+1,'th students details:-\n')
    nm=input('enter name                    :')
    rn=int(input('enter roll number             : '))
    m=float(input('enter twelths mark percentage :'))
    std.append(nm)
    std.append(rn)
    std.append(m)
    rec.append(std)
    mark.append(m)
mark.sort(reverse=True)
for i in range(n):
    for j in range(n):
        if mark[i]==rec[j][2]:
            print(rec[j][0])

