print('enter a sentence:')
s=input().split()
s=list(s)
c=0
for i in range(len(s)):
    if (len(s[i]))==10:
        if s[i][4]=='@':
            c=c+1
print("there are",c,"emails of the format 'xxxx@xxxxx'")
    
