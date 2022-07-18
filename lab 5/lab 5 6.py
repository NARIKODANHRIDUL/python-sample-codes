n=int(input('enter the value for N :'))
i=1
print('odd numbers from 1 to',n,'are :')
for i in range(n+1):
    if i%2==0:
        continue
    print(i)
    


