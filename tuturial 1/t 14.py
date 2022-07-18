k=int(input('enter the cost of first banana :'))
n=int(input('enter the amount of dollars he have :'))
w=int(input('enter the number of bananas to buy :'))
b=k*(w*(w+1))/2 - n
if b>0:
    print('he has to borrow $',b,'from his friend')
else:
    print('no need to borow')
