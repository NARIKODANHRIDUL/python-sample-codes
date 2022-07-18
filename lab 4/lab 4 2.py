a=int(input("enter a 3-digit number : "))
b=a%2
if b==0:
    n1=a%10
    a=int(a/10)
    n2=a%10
    a=int(a/10)
    n3=a%10
    s=n1+n2+n3
    print("the sum of the digits of the number is ",s)
else:
    n1=a%10
    a=int(a/10)
    n2=a%10
    a=int(a/10)
    n3=a%10
    p=n1*n2*n3
    print("the product of the digits of the number is ",p)
    
    
