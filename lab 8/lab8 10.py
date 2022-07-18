def floyd(n):
    num=1
    for x in range(1,n+1):
        for y in range(1,x+1):
            print(num,'\t',end='')
            num+=1
        print()
n=int(input('enter a number :'))
floyd(n)
            
