a='india is my country'
a=a+' '
count=0
maximum=0
word=''
for i in range(len(a)):
    if a[i]==' ':
        if count>maximum:
            maximum=count
            longestword=word
        count=0
        word=''
    else:
        count=count+1
        word=word+a[i]
print(maximum,longestword)

