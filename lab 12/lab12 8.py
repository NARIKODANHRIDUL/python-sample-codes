l=[]
n=int(input("enter number of tries:"))
for i in range(n):
    s =input().split()
    for i in range(1,len(s)):
        s[i]=int(s[i])   
    if s[0]=="append":
        l.append(s[1])
        print(s[1],'added at the end of the list')
    elif s[0]=="extend":    
        l.extend(s[1:])
        print(s[1:],'added at the end of the list')
    elif s[0]=="insert":
        l.insert(s[1],s[2])
        print(s[2],'added at',s[1],'index position')
    elif s[0]=="remove":
        l.remove(s[1])
        print(s[1],'is removed from the list')
    elif s[0]=="pop":
        print(l[-1],'is poped out')
        l.pop()
    elif s[0]=="index":
        print(l.index(s[1]))
    elif s[0]=="count":
        print(l.count(s[1]))
    elif s[0]=="sort":
        l.sort()
    elif s[0]=="reverse":
        l.reverse()
    elif s[0]=="print":
        print(l)

