print(
'''
------MENU------
 SUM                          - 1
 DIFFERENCE                   - 2
 PRODUCT                      - 3
 QUOTIENT                     - 4
 REMINDER                     - 5
 LARGEST OUT OF TWO GIVEN NO. - 6
 ''')
a=int(input('enter CODE:-'))
x=int(input("enter first numner  :"))
y=int(input("enter second numner :"))
if a==1:
    print("the sum is",x+y)
elif a==2:
    print("The difference is",x-y)
elif a==3:
    print("The product is",x*y)
elif a==4:
    print("the quotient is",int(x/y))
elif a==5:
    print("The reminder is",x%y)
elif a==6:
    if x>y:
        print(x," is greater than",y)
    else:
        print(y," is greater than",x)

