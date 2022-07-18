n=int(input('Enter a number :'))
s=str(n)
l=len(s)
f=0
for i in range(l//2):
   if s[i]!=s[l-1-i]:
       f=1
       break
if f==1:
    print('Given number is not a palindrome!!!')
else:
    print('Given number is a palindrome!!!')
      
       
       
    
