a=int(input('enter a value for A: '))
b=int(input('enter a value for B: '))
k=int(input('enter a value for K: '))
p=0
i=1
while i<=k:
    if i%2==1:
        p=p+a
    else:
        p=p-b
    i+=1
    
print('position of the cat after',k,'jumps is',p)
