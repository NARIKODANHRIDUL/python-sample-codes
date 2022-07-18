def pal(n):
    y=str(n)
    for i in range((len(y))//2):
        if y[i]!=y[len(y)-i-1]:
            return 0
    return 1
n=int(input('enter a number :'))
if pal(n)==1:
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')

