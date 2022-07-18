n=int(input('number of sticks drwan by sasha                :'))
k=int(input('number of sticks to be crossed out in each turn :'))
c=int(n/k)
if c%2==0:
    print('NO')
else:
    print('YES')
    
