def pali(s):
    if len(s)==1:
        return 'given string is a palindrome'
    else:
        if s[0]==s[-1]:
            return pali(s[1:-1])
        else:
            return 'given string is not a palindrome'
s=input('enter a string :')
print(pali(s))
