i=input('enter a string:')
for j in range(len(i)):
    if i[j]=='.':
        i=i.replace(i[j+1],i[j+1].upper())
print(i)

                
