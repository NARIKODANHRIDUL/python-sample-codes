a=int(input("enter a number :"))
b=str(a)
s,p=0,1
for l in range(len(b)-1,-1,-1):
    if(l%2==0):
         p=p*int(b[l])
    else:
        s=s+int(b[l])
print(s,"is the sum of numbers at the even position")
print(p,"is the product of numbers at the odd position")
    

 
