rec=[]
for i in range(5):
    a=[]
    print('enter ',i+1,'th students name and 3 subjects seperated by comma:',sep='',end='')
    a=map(str,input().split(','))
    rec.append(list(a))
for i in range(5):
    for j in range(4):
        print(rec[i][j],end=" ")
    print()
        
        
