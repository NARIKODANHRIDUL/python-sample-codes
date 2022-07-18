def strl(s,c):
    if s==' ':
        return c
    else:
        return strl(s[1:],c+1)

s=input('enter a string :')
s=s+' '
print(strl(s,0))
